1. Create a server and install httpd and creating/deploying sample webpage using user data.
    This has been done through the CFT.

2. Managing the configuration part like Rewrite rule for http to https is carried out through Ansible.
   We can even add in the playbook to create httpd server.

3. SSL is enabled for the Rewrite rule. Created self singed cert.

Ansible for installing and configuring the Apache web server :

    Install the necessary packages.
    Maintain the main configuration file.
    Maintain the configuration file for mod_ssl.
    Install custom certificate files.
    Enable and maintain the configuration file for mod_status.
