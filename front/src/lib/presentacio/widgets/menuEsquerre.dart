import 'package:flutter/material.dart';

class MenuEsquerre extends StatelessWidget {
  Widget build(BuildContext context) {
    return ListView(
      children: [
        const DrawerHeader(
          child: Text('Menú'),
        ),
        ListTile(
          title: const Text('Opció 1'),
          onTap: () {
            Navigator.pop(context);
          },
        ),
      ],
    );
  }
}
