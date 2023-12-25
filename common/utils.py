from pathlib import Path


def get_attachment_path():
    home_path = Path(__file__).parent.parent
    attachment_path = home_path.joinpath("attachments")

    if not attachment_path.exists():
        attachment_path.mkdir(parents=True)

    return attachment_path
