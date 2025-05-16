package main

type Point2D struct {
	x float64
	y float64
}

type Segment struct {
	p1 Point2D
	p2 Point2D
}

type Line struct {
	a, b, c float64
}

type Circle struct {
	c Point2D
	r float64
}

func lineFromPts(p1, p2 Point2D) *Line {
	var res Line

	res.a = p2.y - p1.y
	res.b = p1.x - p2.y
	res.c = p2.x*p1.y - p1.x*p2.y

	return &res
}

func lineIntersec(l1, l2 Line) (*Point2D, bool) {
	denominator := l1.a*l2.b - l2.a*l1.b

	if denominator == 0 {
		return nil, false
	}
	x := (l1.b*l2.c - l2.b*l1.c) / denominator
	y := (l2.a*l1.c - l1.a*l2.c) / denominator

	return &Point2D{x, y}, true
}

func segAndLineIntersec(seg Segment, l Line) *Point2D {
	p1, p2 := seg.p1, seg.p2
	line_segment := lineFromPts(p1, p2)
	intersec_p, intersec_f := lineIntersec(l, *line_segment)

	if intersec_f == false {
		return nil
	}

	x, y := intersec_p.x, intersec_p.y

	if min(p1.x, p2.x) <= x && x <= max(p1.x, p2.x) && min(p1.y, p2.y) <= y && y <= max(p1.y, p2.y) {
		return &Point2D{x, y}
	}
	return nil
}

func twoSegsIntersec(seg1, seg2 Segment) *Point2D {
	x1, y1, x2, y2 := seg1.p1.x, seg1.p1.y, seg1.p2.x, seg1.p2.y
	x3, y3, x4, y4 := seg2.p1.x, seg2.p1.y, seg2.p2.x, seg2.p2.y

	a1 := y2 - y1
	b1 := x1 - x2
	c1 := x2*y1 - x1*y2

	a2 := y4 - y3
	b2 := x3 - x4
	c2 := x4*y3 - x3*y4

	denominator := a1*b2 - a2*b1

	if denominator == 0 {
		return nil
	}

	x := (b1*c2 - b2*c1) / denominator
	y := (a2*c1 - a1*c2) / denominator

	if min(x1, x2) <= x && x <= max(x1, x2) &&
		min(y1, y2) <= y && y <= max(y1, y2) &&
		min(x3, x4) <= x && x <= max(x3, x4) &&
		min(y3, y4) <= y && y <= max(y3, y4) {
		return &Point2D{x, y}
	}

	return nil
}

//СТАЛО ВПАДЛУ
