void setup(){
  size(500, 500);
  
}

boolean state = false;


void draw(){
   background(74, 57, 51);
   
  //fun time
  //min 10, max 20
  //int pointsUpperBound = 20;
  //int pointsLowerBound = 10;
  //int points = round(map(mouseX, 0, width, pointsLowerBound, pointsUpperBound));
  
  int points = 10;
  
  //min 90, max width - 20 
  int outerRadiusLowerBound = 90;
  float outerRadius = round(map(mouseY, 0, height, outerRadiusLowerBound, width-20));
  
  float innerRadius = 80;
  float step = TWO_PI/points;

  //saindo das coordenadas do computador para as cartesianas
  translate(width/2, height/2);
  
  beginShape(); 
    for(int i=0; i<=points*2; i++){
      
      if( i % 2 == 0) {
        float x = innerRadius*cos(i*step)/2;
        float y = innerRadius*sin(i*step)/2;    
        vertex(x,y);
      } else {
        float x = outerRadius*cos(i*step)/2;
        float y = outerRadius*sin(i*step)/2;    
        vertex(x,y);
      }
    }
    endShape();
    
    noStroke();
    fill(240, 165, 0);
}
