import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';
import 'package:src/presentacio/home.dart';
import 'package:src/presentacio/screens/mevesClasses.dart';
import 'package:src/presentacio/widgets/menuEsquerre.dart';
import 'package:src/presentacio/widgets/menuInferior.dart';

void main() {
  final controladorPresentacio = ControladorPresentacio();

  runApp(MyApp(controladorPresentacio: controladorPresentacio));
}

class MyApp extends StatefulWidget {
  final ControladorPresentacio controladorPresentacio;

  MyApp({Key? key, required this.controladorPresentacio}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState(controladorPresentacio);
}

class _MyAppState extends State<MyApp> {
  late ControladorPresentacio _controladorPresentacio;

  _MyAppState(ControladorPresentacio controladorPresentacio) {
    _controladorPresentacio = controladorPresentacio;
  }

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(),
      home: Scaffold(
        body: MevesClasses(controladorPresentacio: _controladorPresentacio),
      ),
    );
  }
}
