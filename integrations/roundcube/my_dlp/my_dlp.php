<?php

class my_dlp extends rcube_plugin
{
    public function init()
    {
        $this->add_hook(
            'attachment_upload',
            [$this, 'check_attachment']
        );
    }

    public function check_attachment($args)
    {
        error_log('===== MY_DLP attachment_upload =====');

        error_log(
            print_r($args, true)
        );

        return $args;
    }
}