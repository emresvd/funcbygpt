import openai
import dotenv
import os
import io
import contextlib
import sys

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = io.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def funcbygpt(func):
    def wrapper(*args, **kwargs):
        print_ = False
        return_ = False

        prompt = func(*args, **kwargs)

        if "--print" in prompt:
            print_ = True
            prompt = prompt.replace("--print", "")

        if "--return" in prompt:
            return_ = True
            prompt = prompt.replace("--return", "")

        prompt += "\ntranslate the above algorithm to python code and write only python code"
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        code = completion.choices[0].text.strip()

        print(code) if print_ else None
        if return_:
            with stdoutIO() as s:
                exec(code, dict(globals(), **locals()))
            return s.getvalue()
        else:
            exec(code, dict(globals(), **locals()))
    return wrapper
