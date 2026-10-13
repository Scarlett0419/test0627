/** Tiny `--flag value` / `--flag` argv parser, no dependency needed for it. */
function parseArgs(argv, defaults = {}) {
  const out = { ...defaults };
  for (let i = 0; i < argv.length; i++) {
    const tok = argv[i];
    if (!tok.startsWith("--")) continue;
    const key = tok.slice(2);
    const next = argv[i + 1];
    if (next === undefined || next.startsWith("--")) {
      out[key] = true; // boolean flag
    } else {
      out[key] = next;
      i++;
    }
  }
  return out;
}

module.exports = { parseArgs };
