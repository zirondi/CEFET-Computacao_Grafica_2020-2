class Point{
    constructor(x, y, c, s){
        this.x = x;
        this.y = y;
        this.dragging = false;
        this.pointColor = c;
        this.momentColor = c;
        this.size = s;
        this.mvColor = '#315C2B';
    
    }

    setCoord(x, y){
        this.x = x;
        this.y = y;
    }

    setColor(c){
        this.momentColor = c;
    }

    drawCircle(){
        fill(this.momentColor)
        noStroke();
        circle(this.x, this.y, this.size)
        
    }

    //Mouse Methods
    mousePressed(){
        if(dist(this.x, this.y, mouseX, mouseY) < 10){
            this.dragging = true;
            return true;
        }
        return false;
    }

    mouseDragged(){
        if(this.dragging){
            this.setCoord(mouseX, mouseY);
            this.setColor(this.mvColor);
            return true;
        }
        return false;
    }

    mouseReleased(){
        if(this.dragging){
            this.dragging = false;
            this.setColor(this.pointColor);
            return true;
        }
        return false;
    }
}

const points = []
points.push(new Point(1*window.innerWidth/5, window.innerHeight/2, "#04724D", 10));
points.push(new Point(2*window.innerWidth/5, window.innerHeight/4, "#04724D", 10));
points.push(new Point(3*window.innerWidth/5, 3*window.innerHeight/4, "#04724D", 10));
points.push(new Point(4*window.innerWidth/5, window.innerHeight/2, "#04724D", 10));

function setup() {
    createCanvas(window.innerWidth, window.innerHeight);
}

function mousePressed(){
    points.some((p) => {
        return p.mousePressed()
    })
}

function mouseDragged(){
    points.some((p) => {
        return p.mouseDragged()
    })

}

function mouseReleased(){
    points.some((p) => {
        return p.mouseReleased()
    })

}

function draw() {
    background("#181F1C");
    
    points.forEach((p) => {
        p.drawCircle();
    })

    noFill();
    stroke("#04724D");
    strokeWeight(5);

    beginShape();
    for (let t = 0.01; t <= 1; t += 0.01){

        const ax = points[0].x + t * (points[1].x - points[0].x);
        const ay = points[0].y + t * (points[1].y - points[0].y);

        const bx = points[1].x + t * (points[2].x - points[1].x);
        const by = points[1].y + t * (points[2].y - points[1].y);

        const cx = points[2].x + t * (points[3].x - points[2].x);
        const cy = points[2].y + t * (points[3].y - points[2].y);

        const dx = ax + t * (bx - ax);
        const dy = ay + t * (by - ay);

        const ex = bx + t * (cx - bx);
        const ey = by + t * (cy - by);

        const fx = dx + t * (ex - dx);
        const fy = dy + t * (ey - dy);
    
        vertex(fx, fy);
    }
    endShape();
}