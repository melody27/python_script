<?php

class student{
    public $a;

    public function __construct(){
        $this->a = 'this should be a';
        // extract(array('\$this->a'=>'bbbb'));
        extract(array('cccc'=>'bbbb'));
        var_dump($GLOBALS);
    }

}

$melody = new student();

var_dump($melody->a);



?>