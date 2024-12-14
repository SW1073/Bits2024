import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';

class Home extends StatefulWidget {
  final ControladorPresentacion controladorPresentacion;
  const Home({Key? key, required this.controladorPresentacion});

  @override
  State<Home> createState() => _Home(controladorPresentacion);
}

class _Home extends State<Home> {
  late ControladorPresentacion _controladorPresentacion;

  _Home(ControladorPresentacion controladorPresentacion) {
    _controladorPresentacion = controladorPresentacion;
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
