import os
import subprocess

# لیست متغیرهایی که محیط ریل‌وی را لو می‌دهند
env_to_remove = [
    "RAILWAY_PROJECT_ID", 
    "RAILWAY_CONTAINER_ID", 
    "RAILWAY_SERVICE_ID", 
    "RAILWAY_ENVIRONMENT",
    "RAILWAY_GIT_COMMIT_SHA"
]

current_env = os.environ.copy()
for key in env_to_remove:
    current_env.pop(key, None)

# دانلود و اجرای مستقیم فایل کلاینت بدون داشتن داکر فایل
# این دستور برنامه اصلی را در محیط ایزوله اجرا می‌کند
command = ["curl", "-sL", "https://github.com/traffmonetizer/cli_v2/releases/latest/download/container_core"]
subprocess.run(command, env=current_env)

# اجرای توکن شما
run_command = ["./container_core", "accept", "--token", "1LFGl6tm4mp/8nr8YUfHc0WdrknVPfWT4n1MkDhfvlQ="]
subprocess.run(run_command, env=current_env)
