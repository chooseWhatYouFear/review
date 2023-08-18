import os


class Path:
    root_dir = os.path.dirname(os.path.dirname(__file__))
    env_path = os.path.join(root_dir, 'config/env.toml')


if __name__ == '__main__':
    print(Path.root_dir)