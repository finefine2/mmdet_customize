import os
import json

def convert_text_to_coco(json_dir, out_file):
    anno_id = 0 
    image_id = 0 
    images = [] 
    annotations = []
    for filename in os.listdir(json_dir): 
        if filename.endswith('.json'): 
            with open(os.path.join(json_dir,filename),'r') as f: 
                data = json.load(f) 

            for image in data['images']: 
                if image['name'].endswith('jpeg'): 
                    image['name'] = image['name'].replace('jpeg','jpg')
                elif image['name'].endswith('JPG'): 
                    image['name'] = image['name'].replace('JPG','jpg')
                else: 
                    image['name'] = image['name']
                    
                images.append(dict(
                    id=image_id,
                    file_name=image['name'],
                    height=image['height'],
                    width=image['width']
                ))

            for anno in data['annotations']: 
                for poly, bbox in zip(anno["polygons"],anno["bbox"]):  
                    text = poly["text"]
                    idx = poly["id"]
                    
                    bbox_values = [bbox["x"], bbox["y"], bbox["width"], bbox["height"]]
                
                    area = bbox_values[2] * bbox_values[3]
                    
                    annotations.append(dict(
                        image_id=image_id,
                        id=anno_id,
                        category_id=0,
                        bbox=bbox_values,
                        area=area,
                        segmentation=[poly],
                        iscrowd=0
                    ))                               
                    anno_id += 1
            
            # increment the image id after processing each json file
            image_id += 1
    coco_format = dict(
        images=images,
        annotations=annotations,
        categories=[{'id': 0, 'name': 'text'}])
    
    with open(out_file,'w') as f: 
        json.dump(coco_format,f)


if __name__ == '__main__':
    convert_text_to_coco(json_dir='/raid/new_OCR/medical+finance/samples2/annotations/train',
                         out_file='/raid/new_OCR/medical+finance/samples2/train.json')
                         
    convert_text_to_coco(json_dir='/raid/new_OCR/medical+finance/samples2/annotations/val',
                         out_file='/raid/new_OCR/medical+finance/samples2/val.json')
                         
    convert_text_to_coco(json_dir='/raid/new_OCR/medical+finance/samples2/annotations/test',
                         out_file='/raid/new_OCR/medical+finance/samples2/test.json')
