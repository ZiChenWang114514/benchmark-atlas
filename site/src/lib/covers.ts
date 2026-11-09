function esc(value: string): string {
  return value.replace(/[&<>"']/g, (char) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char] || char
  ));
}

export function newsCover(options: {
  name: string;
  tone: string;
  score: number | null;
  heat: number | null;
  heatMax: number;
  wide?: boolean;
}): string {
  const width = options.wide ? 640 : 360;
  const height = options.wide ? 220 : 140;
  const name = options.name.length > 28 ? `${options.name.slice(0, 26)}…` : options.name;
  const lines = [];
  for (let i = -height; i < width; i += 18) {
    lines.push(`<line x1="${i}" y1="0" x2="${i + height}" y2="${height}" stroke="${options.tone}" stroke-opacity="0.28" stroke-width="2" />`);
  }
  let metric = '';
  if (options.score != null) {
    const bar = Math.max(8, Math.min(width - 36, ((width - 36) * options.score) / 100));
    metric = `<rect x="18" y="${height - 28}" width="${width - 36}" height="8" rx="4" fill="#fffdf8" fill-opacity="0.7" /><rect x="18" y="${height - 28}" width="${bar.toFixed(1)}" height="8" rx="4" fill="${options.tone}" /><text x="${width - 18}" y="${height - 36}" text-anchor="end" fill="#1b1916" font-size="13">${options.score.toFixed(1)}</text>`;
  } else if (options.heat != null && options.heatMax > 0) {
    const bar = Math.max(8, Math.min(width - 36, ((width - 36) * options.heat) / options.heatMax));
    metric = `<rect x="18" y="${height - 28}" width="${width - 36}" height="8" rx="4" fill="#fffdf8" fill-opacity="0.7" /><rect x="18" y="${height - 28}" width="${bar.toFixed(1)}" height="8" rx="4" fill="${options.tone}" /><text x="${width - 18}" y="${height - 36}" text-anchor="end" fill="#1b1916" font-size="13">${options.heat}</text>`;
  }
  return `<svg class="news-cover" viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(name)}"><rect width="${width}" height="${height}" fill="#f8e7b8" />${lines.join('')}<text x="18" y="${metric ? height - 48 : height / 2}" fill="#1b1916" font-size="${options.wide ? 28 : 20}" font-family="Newsreader, serif">${esc(name)}</text>${metric}</svg>`;
}
