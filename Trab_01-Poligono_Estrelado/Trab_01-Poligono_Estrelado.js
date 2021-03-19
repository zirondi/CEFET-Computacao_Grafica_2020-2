function setup() {
    createCanvas(window.innerWidth, window.innerHeight);

}

function windowResized() {
    resizeCanvas(window.innerWidth, window.innerHeight);
}

function draw() {
    background(74, 57, 51);

    const outerRadiusLowerBound = 90;
    const innerRadius = 80;
     
    const outerRadius = map(mouseY, 100, window.innerHeight, outerRadiusLowerBound, window.innerHeight - 500);
    const points = round(map(mouseX, 10, window.innerWidth, 5, 20));


    const step = TWO_PI/points;
    const halfStep = step/2;

    const text_of_points = `The star has ${points} points.`;

    textSize(16)
    text(text_of_points, 20, 20);





    translate(window.innerWidth/2, window.innerHeight/2);
    rotate(frameCount/100);
    beginShape()
    for (let i = 0; i<= TWO_PI; i+=step){
        
        var x = innerRadius * cos(i);
        var y = innerRadius * sin(i);
        vertex(x, y);

        x = outerRadius * cos(i+halfStep);
        y = outerRadius * sin(i+halfStep);
        vertex(x,y);
    }
    endShape();

    noStroke();
    fill(240, 165, 0);
}
