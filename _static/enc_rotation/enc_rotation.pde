import gifAnimation.*;

GifMaker gif;

float angle = 2.5;        // angolo iniziale
float radius = 50;     // raggio del cerchio grande
float speed = 0.5;     // velocità di rotazione

void setup() {
  size(120, 120);
  frameRate(8);
  gif = new GifMaker(this, "animazione.gif");
  gif.setRepeat(0);
}

void draw() {
  background(255);
  
  if (frameCount % 11 == 0)
    speed = speed * -1;

  // centro del cerchio grande
  float cx = width/2;
  float cy = height/2;

  // disegno del cerchio grande (path)
  noFill();
  stroke(200);
  ellipse(cx, cy, radius*2, radius*2);

  // calcolo posizione del cerchietto piccolo
  float x = cx + cos(angle) * radius * 0.75;
  float y = cy + sin(angle) * radius * 0.75;

  // disegno del cerchietto piccolo
  fill(0);
  noStroke();
  ellipse(x, y, 20, 20);
  
  gif.addFrame();
  
  if (frameCount > 22) {
    gif.finish();
    noLoop();
  }

  // aggiorno l'angolo
  angle += speed;
}
