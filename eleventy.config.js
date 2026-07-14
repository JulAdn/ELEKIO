const fs = require("fs");
const path = require("path");

module.exports = function (eleventyConfig) {
  // Passthrough pour les fichiers statiques
  eleventyConfig.addPassthroughCopy({ "src/style.css": "style.css" });
  eleventyConfig.addPassthroughCopy({ "src/images": "images" });
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });

  // Copier les assets racine (logo, favicon, etc.)
  const rootAssets = [
    "logo-elekio-header.png",
    "logo-elekio.png",
    "favicon.png",
    "apple-touch-icon.png",
    "robots.txt",
    "sitemap.xml",
  ];
  rootAssets.forEach((file) => {
    const src = path.join(__dirname, file);
    if (fs.existsSync(src)) {
      eleventyConfig.addPassthroughCopy({ [file]: file });
    }
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    templateFormats: ["njk", "md", "html"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
  };
};
