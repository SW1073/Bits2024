import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';

class MenuEsquerre extends StatefulWidget {
  final ControladorPresentacio controladorPresentacio;

  const MenuEsquerre({Key? key, required this.controladorPresentacio})
      : super(key: key);

  @override
  State<MenuEsquerre> createState() => _MenuEsquerre(controladorPresentacio);
}

class _MenuEsquerre extends State<MenuEsquerre> {
  late ControladorPresentacio _controladorPresentacio;

  _MenuEsquerre(ControladorPresentacio controladorPresentacio) {
    _controladorPresentacio = controladorPresentacio;
  }

  @override
  void initState() {
    super.initState();
  }

  void anarAfegirAules() {
    return _controladorPresentacio.mostraAfegirAules(context);
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        const DrawerHeader(
          child: Center(
            child: Text(
              'Menú',
              style: TextStyle(
                color: Color.fromRGBO(8, 72, 135, 1),
                fontWeight: FontWeight.bold,
                fontSize: 20,
              ),
            ),
          ),
        ),
        ListTile(
          title: Center(
            child: const Text(
              'Afegir aules',
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 20,
              ),
            ),
          ),
          onTap: () {
            anarAfegirAules();
          },
        ),
        ListTile(
          title: Center(
            child: const Text(
              'Tancar sessió',
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 20,
              ),
            ),
          ),
          onTap: () {
            Navigator.pop(context);
          },
        ),
      ],
    );
  }
}
