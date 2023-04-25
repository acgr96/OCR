# OCR
This python script leverages Tesseract's OCR capabilities along with image processing and manipulation through Pillow to pre-process color imagery for character extraction and transformation. The script ties in tkinter file selection tools and is implemented in Jupyter Notebook so that:

&nbsp;&nbsp;&nbsp;&nbsp;i) Users may use the notebook educationally to explore individual image maniupaltion processes in python and also document the different &nbsp;&nbsp;&nbsp;&nbsp;ways in which tesseract can be implemented depeding on the OCR scheme required.

&nbsp;&nbsp;&nbsp;&nbsp;ii) Individual image manipulation processes can be isolated depending on OCR / image requirements for best processing.

The context of this specific script is to extact bathymetry contour data from web imagery to average and apply as generalized bathymetry in 3D geologic models (sample image: Gilman_Bathy.jpg) but the intention is to lay it out in such a way that it may be easily modified and adapted to similiar OCR tasks.

**To do:**
- Improve black/white contrast preprocessing on numeric values to yield more accurate character extraction
- Improve scripting function for seperating unstructured numeric output into appropriate bins/values
- Test implement GDAL and Selenium for scraping and applying script to web based topographic data based on geographic coordinates


