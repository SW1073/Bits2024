import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';

class Home extends StatefulWidget {
  final ControladorPresentacio controladorPresentacio;
  const Home({Key? key, required this.controladorPresentacio});

  @override
  State<Home> createState() => _Home(controladorPresentacio);
}

class _Home extends State<Home> {
  late ControladorPresentacio _controladorPresentacio;

  _Home(ControladorPresentacio controladorPresentacio) {
    _controladorPresentacio = controladorPresentacio;
  }

  @override
  void initState() {
    super.initState();
  }

  void _a() {
    print('a');
  }

  // blau fosc -> Color.fromRGBO(8, 72, 135, 1)
  // aquamarina -> Color.fromRGBO(44, 246, 179, 1)
  // verd -> Color.fromRGBO(73, 160, 120, 1)
  // gris -> Color.fromRGBO(219, 212, 211, 1)

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Column(children: [
      Center(
        child: Ink(
          decoration: const ShapeDecoration(
            color: Color.fromRGBO(219, 212, 211, 1),
            shape: CircleBorder(),
          ),
          child: IconButton(
            onPressed: _a,
            icon: Icon(Icons.add),
            color: Color.fromRGBO(73, 160, 120, 1),
          ),
        ),
      ),
      Center(
        child: Ink(
          decoration: const ShapeDecoration(
            color: Color.fromRGBO(44, 246, 179, 1),
            shape: CircleBorder(),
          ),
          child: IconButton(
            onPressed: _a,
            icon: Icon(Icons.add),
            color: Color.fromRGBO(8, 72, 135, 1),
          ),
        ),
      ),
    ]));
  }
}
