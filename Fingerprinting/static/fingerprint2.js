const target = document.getElementById("target-sentence").textContent.trim();
const typingInput = document.getElementById("typing-input");
const typingResult = document.getElementById("typing-result");
const restartButton = document.getElementById("restart-button");

let startTime = null;
let corrections = 0;
let finished = false;

typingInput.addEventListener("keydown", event => {
  if (finished) return;
  if (startTime === null && event.key.length === 1) {
    startTime = performance.now();
  }
  if (startTime !== null && event.key === "Backspace") {
    corrections++;
  }
});

// A pasted sentence would not measure typing, so this input accepts key presses only.
typingInput.addEventListener("paste", event => event.preventDefault());

typingInput.addEventListener("input", () => {
  // A normal keyboard apostrophe becomes the curly apostrophe in the target.
  typingInput.value = typingInput.value.replaceAll("'", "’");
  if (finished || startTime === null || typingInput.value !== target) return;

  finished = true;
  const seconds = (performance.now() - startTime) / 1000;
  const charactersPerSecond = target.length / seconds;
  typingResult.textContent =
    `Time: ${seconds.toFixed(2)} s | ` +
    `Speed: ${charactersPerSecond.toFixed(2)} characters/s | ` +
    `Backspace corrections: ${corrections}`;
  typingInput.disabled = true;

  fetch("/collect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      kind: "typing",
      timeSeconds: Number(seconds.toFixed(2)),
      charactersPerSecond: Number(charactersPerSecond.toFixed(2)),
      corrections: corrections
    })
  });
});

restartButton.addEventListener("click", () => {
  startTime = null;
  corrections = 0;
  finished = false;
  typingInput.disabled = false;
  typingInput.value = "";
  typingResult.textContent = "";
  typingInput.focus();
});
