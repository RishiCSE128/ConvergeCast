#!/bin/bash
function nnet(){
    interface=wlp3s0
    x=`ifconfig $interface | head -2 | tail -1` ; return $x | cut -d ' ' -f2
    return $x
}

echo $?