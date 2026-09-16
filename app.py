import gradio as gr
import joblib

model = joblib.load("model.pkl")

def prediction(down,ydstogo,yardline_100, score_differential,formation,qtr,time_minutes,time_seconds):
    quarter_seconds_remaining = time_minutes*60+time_seconds
    shotgun = 1.0 if formation == "Shotgun" else 0.0
    X = [[
        down,
        ydstogo,
        yardline_100,
        score_differential,
        qtr,
        shotgun,
        quarter_seconds_remaining
    ]]
 
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    return f'Pass:{round(probabilities[0]*100)}% Run:{round(probabilities[1]*100)}%'

demo = gr.Interface(
    fn=prediction,
    inputs=[gr.Slider(value=2, minimum=1, maximum=4, step=1, label="down"),gr.Slider(value=10, minimum=1, maximum=20, step=1,label="Yards to firstdown"),gr.Slider(value=50, minimum=1, maximum=99, step=1,label="Yards to touchdown"),gr.Slider(value=0, minimum=-35, maximum=35, step=1,label="Point differental(offensive perspective)"),gr.Dropdown(["Shotgun", "Undercenter"], label="Formation"),gr.Slider(value=2, minimum=1, maximum=4, step=1,label="Quarter"),gr.Slider(value=15, minimum=0, maximum=15, step=1,label="Minutes Remaining"),gr.Slider(value=30, minimum=0, maximum=60, step=1,label="Seconds Remaing")],
    outputs=gr.Textbox(label="Prediction"),
    api_name="predict",
    flagging_mode="never"
)

demo.launch()