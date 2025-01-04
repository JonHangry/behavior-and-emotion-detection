Behavior and Facial Expression Recognition System
This project is a system designed to analyze students' behaviors and facial expressions in a classroom environment. By recognizing and interpreting states such as interest, confusion, or boredom, the system provides insights that enable teachers to adjust their teaching strategies flexibly.

Key Features:
Multi-person Detection: Handles crowded environments with multiple individuals, such as classrooms.
State Recognition: Accurately identifies emotional states (e.g., interest, confusion) and actions.
Real-time Analysis: Offers immediate feedback for dynamic teaching adjustments.
Future Applications:
While currently focused on educational settings, this technology has the potential to be applied in other environments, such as:

Factories: Monitoring workers' focus and efficiency.
Offices: Assessing engagement during meetings or work tasks.
This project contributes to improving productivity, engagement, and overall performance in various fields through actionable insights derived from behavior and emotion analysis.

### Train

```
We give an example, more details please see train.py
python trian.py --cfg models/yolov5l.yaml --batch-size 32 --epoch 100 
```

### Inference

```
Please see val.py
```

### Dataset

The dataset format is VOC (.xml). You can use to convert it to COCO(.json) or TXT format. We already provide a script to transfer  xml format to txt format (Please see prepare_data.py).
