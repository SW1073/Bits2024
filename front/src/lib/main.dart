import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';
import 'package:src/presentacio/home.dart';
import 'package:src/presentacio/screens/mevesClasses.dart';
import 'package:src/presentacio/widgets/menuEsquerre.dart';
import 'package:src/presentacio/widgets/menuInferior.dart';

void main() {
  final controladorPresentacion = ControladorPresentacion();

  runApp(MyApp(controladorPresentacion: controladorPresentacion));
}

class MyApp extends StatefulWidget {
  final ControladorPresentacion controladorPresentacion;

  MyApp({Key? key, required this.controladorPresentacion}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState(controladorPresentacion);
}

class _MyAppState extends State<MyApp> {
  late ControladorPresentacion _controladorPresentacion;

  _MyAppState(ControladorPresentacion controladorPresentacion) {
    _controladorPresentacion = controladorPresentacion;
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
        appBar: AppBar(
          title: const Text(
            'Nom App',
            style: TextStyle(
              color: Color.fromRGBO(8, 72, 135, 1),
              fontWeight: FontWeight.bold,
            ),
          ),
          leading: Builder(
            builder: (context) {
              return IconButton(
                icon: const Icon(Icons.menu),
                onPressed: () {
                  Scaffold.of(context).openDrawer();
                },
              );
            },
          ),
        ),
        body: MevesClasses(controladorPresentacion: _controladorPresentacion),
        drawer: Drawer(
          child: MenuEsquerre(),
        ),
        bottomNavigationBar: MenuInferior(),
      ),
    );
  }
}
