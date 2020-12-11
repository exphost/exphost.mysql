def test_user1(host):
    u = host.user("user1")
    assert u.exists
    assert u.name == "user1"
    assert u.group == "user1"
    assert u.uid == 2000
    assert u.gid == 2000

def test_user2(host):
    u = host.user("user2")
    assert u.exists
    assert u.name == "user2"
    assert u.group == "user2"
    assert u.uid == 2001
    assert u.gid == 2001
    assert u.home == "/home/zzzz"

def test_user3(host):
    u = host.user("user3")
    assert u.exists
    assert u.name == "user3"
    assert u.group == "user3"
    assert u.uid == 2002
    assert u.gid == 2002
#   sudo and tty problem
#    with host.sudo():
#        assert u.password == "$6$mysecretsalt$MIJffjeQyfrKKrGkprGrDL/g2mCJa53koLmYQuuLmY9y37pDvGKPXU1Ov3RbMi.tpQ9cWvxAzUVtBLe7KrZoU."

def test_user4(host):
    u = host.user("user4")
    assert u.exists
    assert u.name == "user4"
    assert u.group == "user4"
    assert u.uid == 2004
    assert u.gid == 2004
#   sudo and tty problem
#    with host.sudo():
#        authorized = host.file("/home/user4/.ssh/authorized_keys")
#        assert authorized.exists
#        assert authorized.is_file
#        assert authorized.contains("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDZDxIASdx2QeV/6Qm+Y3VzFl9FB5Bjh4YH/9KrrUrOERnVHgSUuLt87D2rjB6R+r3j+eVsTXFrWFr3wLUAbjU+z922jSKOXiTa9XStUj4DTjkSLXTwTqjCabdKEt1g53wvzSHMH5LQCDhvyj3rQXqq+aw+qwSVJdY2Y/d/MuB0tOi61+j8A7/Oo8wVQPj1QVHLxcORrzZwSi4b1/tjn6jk/2q1vKgmlCxaeyDK+htf9IP8W+Kmwp8BUvzlDXrntAijOXmuc2DQopc4sQ4XYiBaiTZ2bvtu+mY2mLZSba4zLws1uLEfvawSdXDjnFdy1CgYgYeJYMqWl0AmnPIqkF4428LawbEDOX2VzNGjR+CcrON/GC3LOIAjKFVMSSIImgzLtSz60cN9rIdggp7w2GA03NdQ7khlNTPRrh7RbLnt2obcbUzRRQ2dWoSD9RqVueYmtWhN8YH2Cy2bLtVtkDBN6YKo+dSdoJ69yit+WeD+e/ldI/ORRUp6WCvTFiOqwqc= torgiren@redraptor")

