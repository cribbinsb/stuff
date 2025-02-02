import cv2
import stuff.coord as coord

def draw_line(img, start, stop, clr=None, thickness=1):
    height, width, _ = img.shape
    p0=[int(coord.clip01(start[0])*width), int(coord.clip01(start[1])*height)]
    p1=[int(coord.clip01(stop[0])*width), int(coord.clip01(stop[1])*height)]
    if clr is None:
        clr=(255, 255, 255)
    cv2.line(img, p0, p1, clr, thickness=thickness)

def draw_box(img, box, clr=None, thickness=1):
    height, width, _ = img.shape
    p0=[int(coord.clip01(box[0])*width), int(coord.clip01(box[1])*height)]
    p1=[int(coord.clip01(box[2])*width), int(coord.clip01(box[3])*height)]
    if clr is None:
        clr=(255, 255, 255)
    cv2.rectangle(img, p0, p1, clr, thickness)

def draw_circle(img, centre, radius, clr=None, thickness=1):
    height, width, _ = img.shape
    p=[int(coord.clip01(centre[0])*width), int(coord.clip01(centre[1])*height)]
    r=int(radius*width+0.5)
    cv2.circle(img, p, r, clr, -1)

def draw_text(img, text, xc, yc, img_bg=None,
              font=cv2.FONT_HERSHEY_SIMPLEX,
              fontScale=0.65,
              fontColor=(128,255,255),
              bgColor=(0,0,0),
              lineType=2,
              thickness=1
              ):
    height, width, _ = img.shape
    x=(int)(xc*width)
    y=(int)(yc*height)
    text_split=text.split("\n")

    if img_bg is None:
        img_bg=img

    for t in text_split:
        xp=x
        yp=y
        (text_width, text_height) = cv2.getTextSize(t,
                                                    font,
                                                    fontScale=fontScale,
                                                    thickness=thickness)[0]
        box_coords = ((xp, yp+2),
                      (xp + text_width + 2, yp - text_height - 2))
        y+=text_height+5
        
        cv2.rectangle(img_bg, box_coords[0], box_coords[1], bgColor, cv2.FILLED)
        cv2.putText(img,
                    t,
                    (xp, yp),
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
