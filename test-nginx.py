import testinfra

def test_nginx_is_installed(host):
   nginx = host.package("nginx")
   assert nginx.is_installed

# def test_nginx_running_and_enabled(host):
#    nginx = host.service("nginx")
#    assert nginx.is_running
#    assert nginx.is_enabled

def test_file_exists(host):
    file = host.file("/etc/passwd")
    assert file.is_file

def test_process(host):
    nginx = host.process.get(user="root", comm="nginx")
    assert nginx