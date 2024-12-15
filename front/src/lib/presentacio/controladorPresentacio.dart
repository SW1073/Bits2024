import 'package:flutter/material.dart';
import 'package:src/presentacio/screens/afegirAules.dart';
import 'package:src/presentacio/screens/aula.dart';
import 'package:src/presentacio/screens/mevesClasses.dart';

class ControladorPresentacio {
  void mostraAula(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => Aula(
          controladorPresentacio: this,
        ),
      ),
    );
  }

  void mostraMevesAules(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => MevesClasses(
          controladorPresentacio: this,
        ),
      ),
    );
  }

  void mostraAfegirAules(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => AfegirAules(
          controladorPresentacio: this,
        ),
      ),
    );
  }
}
