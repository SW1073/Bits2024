import 'package:flutter/material.dart';

class MenuEsquerre extends StatelessWidget {
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
            Navigator.pop(context);
          },
        ),
      ],
    );
  }
}
