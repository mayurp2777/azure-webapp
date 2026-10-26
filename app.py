
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Modern Flask App</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
                font-family: Arial, sans-serif;
                color: white;
                background: linear-gradient(
                    135deg, #0f172a, #1e1b4b, #312e81
                );
            }

            .container {
                width: 100%;
                max-width: 650px;
                padding: 55px 30px;
                text-align: center;
                border: 1px solid rgba(255, 255, 255, 0.18);
                border-radius: 28px;
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(15px);
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.3);
                animation: appear 0.8s ease;
            }

            .badge {
                display: inline-block;
                padding: 9px 16px;
                margin-bottom: 25px;
                border-radius: 30px;
                color: #86efac;
                background: rgba(34, 197, 94, 0.12);
                border: 1px solid rgba(134, 239, 172, 0.25);
                font-size: 13px;
                letter-spacing: 1px;
            }

            h1 {
                margin-bottom: 20px;
                font-size: clamp(38px, 8vw, 58px);
                font-weight: 800;
                letter-spacing: -2px;
                background: linear-gradient(90deg, #60a5fa, #c084fc);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            p {
                margin: 0 auto 28px;
                max-width: 450px;
                color: #cbd5e1;
                font-size: 17px;
                line-height: 1.8;
            }

            .button {
                display: inline-block;
                padding: 15px 28px;
                border-radius: 12px;
                color: white;
                background: linear-gradient(90deg, #2563eb, #7c3aed);
                text-decoration: none;
                font-weight: bold;
                transition: transform 0.25s, box-shadow 0.25s;
            }

            .button:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
            }

            .tech {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 35px;
            }

            .tech span {
                padding: 9px 14px;
                border-radius: 9px;
                background: rgba(255, 255, 255, 0.08);
                color: #cbd5e1;
                font-size: 13px;
            }

            footer {
                margin-top: 35px;
                color: #94a3b8;
                font-size: 13px;
            }

            @keyframes appear {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @media (max-width: 480px) {
                .container {
                    padding: 40px 20px;
                }

                p {
                    font-size: 15px;
                }
            }
        </style>
    </head>

    <body>
        <main class="container">
            <div class="badge">● &nbsp; FLASK APP · RUNNING</div>

            <h1>Hello, World!</h1>

            <p>
                Welcome to my modern web application.
                Built with Python and Flask, ready for the cloud.
            </p>

            <a class="button" href="https://azure.microsoft.com/">
                Explore Microsoft Azure &rarr;
            </a>

            <div class="tech">
                <span>🐍 Python</span>
                <span>⚡ Flask</span>
                <span>☁️ Azure Ready</span>
            </div>

            <footer>
                Crafted with Python · Powered by Flask
            </footer>
        </main>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
