import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';
import 'package:src/presentacio/widgets/menuEsquerre.dart';

class MevesClasses extends StatefulWidget {
  final ControladorPresentacio controladorPresentacio;

  const MevesClasses({Key? key, required this.controladorPresentacio})
      : super(key: key);

  @override
  State<MevesClasses> createState() => _MevesClasses(controladorPresentacio);
}

class _MevesClasses extends State<MevesClasses> {
  late ControladorPresentacio _controladorPresentacio;

  _MevesClasses(ControladorPresentacio controladorPresentacio) {
    _controladorPresentacio = controladorPresentacio;
  }

  @override
  void initState() {
    super.initState();
  }

  // blau fosc -> Color.fromRGBO(8, 72, 135, 1)
  // aquamarina -> Color.fromRGBO(44, 246, 179, 1)
  // verd -> Color.fromRGBO(73, 160, 120, 1)
  // gris -> Color.fromRGBO(219, 212, 211, 1)

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Padding(
          padding: EdgeInsets.only(top: 100, bottom: 100),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Image.asset(
                '../assets/logo.png',
                width: 60,
                height: 60,
                fit: BoxFit.cover,
              ),
              SizedBox(
                width: 20,
              ),
              const Text(
                'Xarxair',
                style: TextStyle(
                  color: Color.fromRGBO(8, 72, 135, 1),
                  fontWeight: FontWeight.bold,
                  fontSize: 40,
                ),
              ),
            ],
          ),
        ),
        leading: Builder(
          builder: (context) {
            return IconButton(
              icon: const Icon(
                Icons.menu,
                color: Color.fromRGBO(8, 72, 135, 1),
              ),
              onPressed: () {
                Scaffold.of(context).openDrawer();
              },
            );
          },
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              margin: const EdgeInsets.symmetric(
                vertical: 10,
                horizontal: 20,
              ),
              child: Text(
                'Les meves classes',
                style: TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                  color: Color.fromRGBO(8, 72, 135, 1),
                ),
              ),
            ),
            const SizedBox(height: 20),
            Expanded(
              child: ListView.builder(
                itemCount: 4,
                itemBuilder: (context, index) {
                  return GestureDetector(
                    onTap: () {
                      _controladorPresentacio.mostraAula(context);
                      print("Tapped on class $index");
                    },
                    child: Container(
                      margin: const EdgeInsets.symmetric(
                        vertical: 10,
                        horizontal: 40,
                      ),
                      padding: const EdgeInsets.all(16.0),
                      decoration: BoxDecoration(
                        color: Color.fromRGBO(219, 212, 211, 1),
                        borderRadius: BorderRadius.circular(12.0),
                      ),
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text(
                            'Nom: Nom complet de nen',
                            style: TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                              color: Color.fromRGBO(8, 72, 135, 1),
                            ),
                          ),
                          const SizedBox(height: 10),
                          Text(
                            'Nom escola: Escola A',
                            style: TextStyle(
                              fontSize: 18,
                              color: Colors.black,
                            ),
                          ),
                          const SizedBox(height: 10),
                          Text(
                            'Provincia escola: Barcelona',
                            style: TextStyle(
                              fontSize: 18,
                              color: Colors.black,
                            ),
                          ),
                          const SizedBox(height: 10),
                          Text(
                            'Nivell: Primaria',
                            style: TextStyle(
                              fontSize: 18,
                              color: Colors.black,
                            ),
                          ),
                          const SizedBox(height: 10),
                          Text(
                            'Linea: 3A',
                            style: TextStyle(
                              fontSize: 18,
                              color: Colors.black,
                            ),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
      drawer: Drawer(
        backgroundColor: Color.fromRGBO(219, 212, 211, 1),
        child: MenuEsquerre(),
      ),
    );
  }
}
