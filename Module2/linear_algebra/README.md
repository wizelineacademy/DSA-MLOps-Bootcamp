---

Create poetry environment
---


To activate poetry environment successfully follow the next step by step:


- Install python version 3.10
    ```
        pyenv install 3.10
    ```
- Install poetry
    ```
        pip install poetry
    ```
- Create virtual poetry env
    ```
        poetry env use 3.10
    ```
    or
    ```
        poetry shell
    ```
- Activate virtual env (if it is not activated)
    ```
        source $(poetry env info --path)/bin/activate
    ```
- Install packages
    ```
        $ poetry install
    ```
- Look for env name
    ```
        poetry env info --path
    ```
- Add environment to jupyter kernel, replace env_name with your environment name
    ```
        python -m ipykernel install --user --name=env_name
    ```

Now you're ready to go!

Alternative with virtualenv
- Install python version 3.10
    ```
        pyenv install 3.10
    ```

- Install virtual env
    ```
        python -m pip install --user virtualenv
    ```
- Create virtual env with virtualenv, replace env_name with your environment name
    ```
        python -m venv env_name
    ```
- Activate environment
    ```
        source env_name/bin/activate
    ```
- Install dependences
    ```
        pip install -r requirements.txt
    ```
- Add environment to jupyter kernel, replace env_name with your environment name
    ```
        python -m ipykernel install --user --name=env_name
    ```


Now you're ready to go!