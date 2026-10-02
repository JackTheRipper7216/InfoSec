// Read features from several browser objects and show what was collected.
const features = {
  language: navigator.language,
  logicalCores: navigator.hardwareConcurrency ?? "unavailable",
  screenSize: `${screen.width} x ${screen.height}`,
  colorDepth: screen.colorDepth,
  windowSize: `${window.innerWidth} x ${window.innerHeight}`,
  pixelRatio: window.devicePixelRatio,
  timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
  referrer: document.referrer || "(direct visit)"
};

const featureOutput = document.getElementById("feature-output");
featureOutput.innerHTML = "";
for (const [name, value] of Object.entries(features)) {
  const item = document.createElement("li");
  item.textContent = `${name}: ${value}`;
  featureOutput.appendChild(item);
}

fetch("/collect", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ kind: "active", ...features })
});

// Keep the order fixed. Typing data is left out because it changes between tries.
const parts = [
  features.language,
  features.screenSize,
  features.colorDepth,
  features.pixelRatio,
  features.timeZone,
  features.logicalCores
];

async function makeFingerprint() {
  const bytes = new TextEncoder().encode(JSON.stringify(parts));
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  const hash = Array.from(new Uint8Array(digest), byte =>
    byte.toString(16).padStart(2, "0")
  ).join("");
  document.getElementById("fingerprint-output").textContent = hash;

  // This second request contains only the hash, not the raw features.
  fetch("/collect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ kind: "fingerprint", sha256: hash })
  });
}

makeFingerprint();
