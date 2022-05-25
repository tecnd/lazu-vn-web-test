# lazu-vn-web-test

Web version of Lazulight: By Your Side.

## Notes:

- It's playable, but noticably choppy.
  - The history menu is VERY laggy, needs to be looked into.
- Eats like, 2 GB of RAM. Because why not.
- Requires an experimental version of Ren'Py (prerelease 7.5.0) to work on Chrome and Safari.
  - Safari may encounter additional issues.
  - Firefox master race.
- No video support.
  - Instead, it asks if you want to open a new browser tab to YouTube.
  - The loading transition was removed.
- Assets have been aggressively reduced to both save on bandwidth requirement and reduce the amount of image processing.
  - Audio was converted to 96kbps Opus.
  - BGs and CGs were cropped and scaled to 1920x1080 WebP.
  - Sprites were cropped and scaled to whatever the transforms would have cropped and scaled them to.
  - Full bundle size is 84 MB!
- BGMs, BGs, and CGs are downloaded on-demand instead of all at the beginning.
  - Audio may take a second to start playing (SFXs are fine).
  - BGs and CGs may look blurry for a second before the file finishes downloading.
  - Reduces initial bundle size to 31 MB!
