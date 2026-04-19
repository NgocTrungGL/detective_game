let currentLevel = 1;
let currentHints = [];
let currentBGM = null;
let introPlayed = false;
const totalLevels = window.GAME_DATA.length;

const bgmIntro = document.getElementById("bgm-intro");
const bgmPhase1 = document.getElementById("bgm-phase-1");
const bgmPhase2 = document.getElementById("bgm-phase-2");
const bgmPhase3 = document.getElementById("bgm-phase-3");
const bgmEnd = document.getElementById("bgm-end");
const sfxTyping = document.getElementById("sfx-typing");
const sfxCorrect = document.getElementById("sfx-correct");
const musicVolume = 0.4;

bgmIntro.volume = musicVolume;
bgmPhase1.volume = musicVolume;
bgmPhase2.volume = musicVolume;
bgmPhase3.volume = musicVolume;
bgmEnd.volume = 0.6;
sfxTyping.volume = 0.5;

function tryPlayIntro() {
  if (!introPlayed && document.getElementById("intro-screen").style.display !== "none") {
    bgmIntro
      .play()
      .then(() => {
        introPlayed = true;
        currentBGM = bgmIntro;
      })
      .catch(() => {});
  }
}

function switchBGM(newBGM) {
  if (currentBGM !== newBGM) {
    if (currentBGM) {
      currentBGM.pause();
      currentBGM.currentTime = 0;
    }
    if (newBGM) {
      newBGM.play().catch(() => {});
      currentBGM = newBGM;
    }
  }
}

function startGame() {
  document.getElementById("intro-screen").style.display = "none";
  document.getElementById("game-area").style.display = "block";
  loadLevel(currentLevel);
}

function loadLevel(id) {
  resetHints();

  if (id >= 1 && id <= 3) switchBGM(bgmPhase1);
  else if (id >= 4 && id <= 6) switchBGM(bgmPhase2);
  else if (id >= 7 && id <= 9) switchBGM(bgmPhase3);

  const data = window.GAME_DATA[id - 1];
  if (!data) {
    finishGame();
    return;
  }

  document.getElementById("level-title").innerText = data.title;
  document.getElementById("progress-text").innerText = `${id}/${totalLevels}`;

  const storyContainer = document.getElementById("story-text");
  typeWriterHTML(data.story, storyContainer, 40);

  document.getElementById("answer-input").value = "";
  document.getElementById("feedback-msg").innerText = "";
  document.getElementById("feedback-msg").className = "";

  currentHints = data.hints;
  document.getElementById("progress-fill").style.width = `${((id - 1) / totalLevels) * 100}%`;
}

function typeWriterHTML(htmlText, element, speed) {
  element.innerHTML = "";
  let i = 0;
  sfxTyping.pause();
  sfxTyping.currentTime = 0;
  sfxTyping.play().catch(() => {});

  function type() {
    if (i < htmlText.length) {
      if (htmlText.charAt(i) === "<") {
        let tag = "";
        while (htmlText.charAt(i) !== ">" && i < htmlText.length) {
          tag += htmlText.charAt(i);
          i++;
        }
        tag += ">";
        i++;
        element.innerHTML += tag;
      } else {
        element.innerHTML += htmlText.charAt(i);
        i++;
      }
      setTimeout(type, speed);
    } else {
      sfxTyping.pause();
    }
  }

  type();
}

function resetHints() {
  for (let i = 0; i < 3; i++) {
    const box = document.getElementById(`hint-box-${i}`);
    box.classList.remove("revealed");
    box.querySelector(".hint-content").innerText = "??? (クリック)";
  }
}

function revealHint(index) {
  const box = document.getElementById(`hint-box-${index}`);
  if (!box.classList.contains("revealed")) {
    box.classList.add("revealed");
    box.querySelector(".hint-content").innerText = currentHints[index];
  }
}

function normalizeAnswer(value) {
  return value.normalize("NFKC").trim();
}

function submitAnswer() {
  const input = document.getElementById("answer-input").value;
  const feedback = document.getElementById("feedback-msg");
  const currentLevelData = window.GAME_DATA[currentLevel - 1];

  if (!currentLevelData) {
    finishGame();
    return;
  }

  const userAnswer = normalizeAnswer(input);
  const isCorrect = currentLevelData.answers.some(
    (answer) => normalizeAnswer(answer) === userAnswer
  );

  if (isCorrect) {
    sfxCorrect.play().catch(() => {});
    feedback.innerText = "データが一致！復号中…";
    feedback.className = "success";
    showSuccessModal(currentLevelData.full_sentence, currentLevelData.translation_vi);
  } else {
    feedback.innerText = "残念！ヒントを使ってみましょう。";
    feedback.className = "error";
    const answerInput = document.getElementById("answer-input");
    answerInput.classList.add("shake");
    setTimeout(() => answerInput.classList.remove("shake"), 500);
  }
}

function showSuccessModal(jp, vi) {
  document.getElementById("modal-jp").innerHTML = jp;
  document.getElementById("modal-vi").innerText = vi;

  const modal = document.getElementById("success-modal");
  modal.style.display = "flex";
  modal.classList.add("fade-in");
}

function nextLevel() {
  document.getElementById("success-modal").style.display = "none";
  currentLevel++;
  loadLevel(currentLevel);
}

function finishGame() {
  document.getElementById("game-area").style.display = "none";
  document.getElementById("end-screen").style.display = "block";
  switchBGM(bgmEnd);
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("answer-input").addEventListener("keypress", (event) => {
    if (event.key === "Enter") submitAnswer();
  });
});
