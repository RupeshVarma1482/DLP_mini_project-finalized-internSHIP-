<?php

$config['plugins'] = [
    'my_dlp'
];

$config['imap_host'] = [
    'ssl://imap.gmail.com:993' => 'Gmail',
    'ssl://outlook.office365.com:993' => 'Outlook'
];

$config['smtp_host'] = [
    'imap.gmail.com' => 'ssl://smtp.gmail.com:465',
    'outlook.office365.com' => 'ssl://smtp.office365.com:465'
];

$config['smtp_user'] = '%u';
$config['smtp_pass'] = '%p';

include(__DIR__ . '/config.docker.inc.php');