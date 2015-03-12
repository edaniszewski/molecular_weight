/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

grammar molecularWeight;

options {
        language=Python;
}

molecule
    : elements+
    ;

elements
    : (ELEMENT QTY?)
    ;

ELEMENT 
    : 'H'
    | 'C'
    | 'O'
    | 'S' 
    ;

QTY
    : [0-9]+
    ;
