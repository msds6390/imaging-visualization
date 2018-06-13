/* MSDS 6390 Assignment 5: Imaging Visualization
 Mosaic portrait of Anthony Bourdain
 Team: Jostein Barry-Straume, Brian Yu 
 Sources:  https://www.youtube.com/watch?v=nnlAH1zDBDE
           https://github.com/hardikvasa/google-images-download
           https://poanchen.github.io/blog/2016/11/15/how-to-add-background-music-in-processing-3.0*/

import processing.sound.*;
SoundFile audioFile;
String audioName = "anthonyBourdainPartsUnknownThemeSong.mp3";
String audioPath;

// Setting global variables
PImage bourdain;
PImage smallerBourdain;
PImage[] allImages;                // array of all images
float[] brightness;                // array of brightness values? 
PImage[] brightImages;

int scale = 8;                     // scale factor - size of each square
int w, h;

void setup() {
  // Load "Parts Unknown" theme song
  audioPath = sketchPath(audioName);
  audioFile = new SoundFile(this, audioPath);  // open mp3 music track
  audioFile.loop();                            // play music track
  
  size(710, 473);
  bourdain = loadImage("bourdainImage.jpg");

  // dynamically load all the images in the directory
  // This function returns all the files in a directory
  File[] files = listFiles(sketchPath("data"));
  allImages = new PImage[files.length-1];      // to ignore the thumbs.db file
  brightness = new float[allImages.length];    // new array brightness
  brightImages = new PImage[256];              // new array brightImages is an array with 256 brightness value

  for (int i = 0; i < allImages.length; i ++) {
    String fileName = files[i].toString();  
    PImage img = loadImage(fileName);          // an array containing all the images

    allImages[i] = createImage(scale, scale, RGB);
    allImages[i].copy(img, 0, 0, img.width, img.height, 0, 0, scale, scale);
    allImages[i].loadPixels();
    float avg = 0;

    // loop through all the pixels examing every pixel, adds up all the brightness values, then
    // averages the sum of the brightness values.
    for (int j = 0; j < allImages[i].pixels.length; j ++) {
      float b = brightness(allImages[i].pixels[j]);
      avg += b;
    }
    avg /= allImages[i].pixels.length;
    brightness[i] = avg;
  }
  printArray(allImages);

  // Loop to fill array brightImage with the image that's the closest in distance to the particular brightness value
  for (int i = 0; i < brightImages.length; i ++) {
    float record = 256;
    for (int j = 0; j < brightness.length; j ++) {
      // Assesing all images and calculating the differences of the current brightness minus that for a particular image 
      float diff = abs(i - brightness[j]);
      // Finds the one with the smallest difference between the target and then saving record
      if (diff < record) {
        record = diff;
        brightImages[i] = allImages[j];
      }
    }
  }
  w = bourdain.width/scale;
  h = bourdain.height/scale;
  smallerBourdain = createImage(w, h, RGB);
  smallerBourdain.copy(bourdain, 0, 0, bourdain.width, bourdain.height, 0, 0, w, h);
}

void draw() {
  //SoundFile.play();
  smallerBourdain.loadPixels();

  // looking at every single pixel of the image
  for (int x = 0; x < w; x ++) {
    for (int y = 0; y < h; y ++) {
      int index = x + y * w; 
      color c = smallerBourdain.pixels[index];
      int imageIndex = int(brightness(c));

      // This is the array that contains all the images indexed by brightness
      // draws the one corresponding to that brightness and dynamically resizing the images
      image(brightImages[imageIndex], x*scale, y*scale, scale, scale);
    }
  }
  // draw once
  //noLoop();
}
