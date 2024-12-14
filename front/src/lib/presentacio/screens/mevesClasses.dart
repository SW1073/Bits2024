import 'package:flutter/material.dart';
import 'package:src/presentacio/controladorPresentacio.dart';

class MevesClasses extends StatefulWidget {
  final ControladorPresentacion controladorPresentacion;

  const MevesClasses({Key? key, required this.controladorPresentacion})
      : super(key: key);

  @override
  State<MevesClasses> createState() => _MevesClasses(controladorPresentacion);
}

class _MevesClasses extends State<MevesClasses> {
  late ControladorPresentacion _controladorPresentacion;

  _MevesClasses(ControladorPresentacion controladorPresentacion) {
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
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Title widget
            Text(
              'Les meves classes',
              style: TextStyle(
                fontSize: 30,
                fontWeight: FontWeight.bold,
                color: Color.fromRGBO(8, 72, 135, 1),
              ),
            ),
            const SizedBox(height: 20),
            Expanded(
              child: ListView.builder(
                itemCount: 4,
                itemBuilder: (context, index) {
                  return GestureDetector(
                    onTap: () {
                      print("Tapped on class $index");
                    },
                    child: Container(
                      margin: const EdgeInsets.symmetric(vertical: 10),
                      padding: const EdgeInsets.all(16.0),
                      decoration: BoxDecoration(
                        color: Color.fromRGBO(219, 212, 211, 1),
                        borderRadius: BorderRadius.circular(12.0),
                      ),
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text(
                            'Nom de classe',
                            style: TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                              color: Color.fromRGBO(8, 72, 135, 1),
                            ),
                          ),
                          const SizedBox(height: 10),
                          Text(
                            'Nom de nen',
                            style: TextStyle(
                              fontSize: 18,
                              color: Colors.black54,
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
    );
  }
}
