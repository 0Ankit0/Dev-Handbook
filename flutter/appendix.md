# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: Widget Quick Reference

### Layout Widgets

| Widget | Purpose |
|--------|---------|
| `Column` | Stack children vertically |
| `Row` | Stack children horizontally |
| `Stack` | Layer children on top of each other |
| `Container` | Box with padding, margin, decoration, size |
| `SizedBox` | Fixed-size space or constrain a child |
| `Expanded` | Fill remaining space in Row/Column |
| `Flexible` | Fill proportional space (flex factor) |
| `Padding` | Add padding around a child |
| `Center` | Center a child in its parent |
| `Align` | Align a child within its parent |
| `Wrap` | Flow children, wrapping to next line |

### Scrolling

| Widget | Purpose |
|--------|---------|
| `ListView` | Scrollable list of children |
| `ListView.builder` | Lazy list (builds only visible items) |
| `GridView` | Scrollable grid |
| `GridView.builder` | Lazy grid |
| `SingleChildScrollView` | Scroll a single widget |
| `CustomScrollView` | Scrollable with slivers (SliverAppBar, etc.) |

### Input Widgets

| Widget | Purpose |
|--------|---------|
| `TextField` | Text input field |
| `TextFormField` | TextField with form validation |
| `ElevatedButton` | Filled button |
| `TextButton` | Flat button |
| `OutlinedButton` | Outlined button |
| `IconButton` | Tappable icon |
| `Checkbox` | Boolean checkbox |
| `Switch` | Toggle switch |
| `Slider` | Range slider |
| `DropdownButton` | Select from list |

### Display Widgets

| Widget | Purpose |
|--------|---------|
| `Text` | Display text |
| `RichText` | Multi-style text |
| `Image` | Display image |
| `Icon` | Material icon |
| `CircularProgressIndicator` | Spinning loading indicator |
| `LinearProgressIndicator` | Bar loading indicator |
| `Card` | Elevated surface container |
| `Divider` | Horizontal separator |
| `Chip` | Label/tag widget |
| `Tooltip` | Hover/long-press tooltip |

---

## Appendix B: Navigation Reference

```dart
// Push a new route onto the stack (go forward)
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => const DetailPage()),
);

// Push and replace current route (no back button)
Navigator.pushReplacement(
  context,
  MaterialPageRoute(builder: (context) => const HomePage()),
);

// Pop (go back)
Navigator.pop(context);

// Pop with a result
Navigator.pop(context, 'result_value');

// Push and wait for result
final result = await Navigator.push<String>(
  context,
  MaterialPageRoute(builder: (context) => const SelectionPage()),
);
// result contains whatever was passed to Navigator.pop()

// Named routes (defined in MaterialApp)
Navigator.pushNamed(context, '/detail', arguments: item);
```

### GoRouter (go_router package) — Recommended for complex navigation

```dart
// pubspec.yaml: go_router: ^13.0.0

final router = GoRouter(
  routes: [
    GoRoute(path: '/', builder: (ctx, state) => const HomePage()),
    GoRoute(
      path: '/detail/:id',
      builder: (ctx, state) {
        final id = state.pathParameters['id']!;
        return DetailPage(id: id);
      },
    ),
  ],
);

// Navigate
context.go('/detail/42');
context.push('/settings');
context.pop();
```

---

## Appendix C: State Management Patterns

### setState (simple local state)

```dart
class CounterWidget extends StatefulWidget {
  const CounterWidget({super.key});
  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _count = 0;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Count: $_count'),
        ElevatedButton(
          onPressed: () => setState(() => _count++),
          child: const Text('Increment'),
        ),
      ],
    );
  }
}
```

### Provider (shared state, recommended for medium apps)

```dart
// 1. Define your state class
class CartModel extends ChangeNotifier {
  final List<String> _items = [];

  List<String> get items => List.unmodifiable(_items);

  void add(String item) {
    _items.add(item);
    notifyListeners();  // triggers rebuild of listeners
  }
}

// 2. Provide at the top of the widget tree
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => CartModel(),
      child: const MyApp(),
    ),
  );
}

// 3. Consume in any widget below
class CartPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final cart = context.watch<CartModel>();  // rebuilds when cart changes
    return ListView(
      children: cart.items.map((i) => Text(i)).toList(),
    );
  }
}

// 4. Mutate without rebuilding
void _addItem(BuildContext context) {
  context.read<CartModel>().add('Apple');  // no rebuild in this widget
}
```

### Riverpod (recommended for large apps)

```dart
// Define provider (global, outside widgets)
final counterProvider = StateProvider<int>((ref) => 0);

// Read and watch
class CounterPage extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final count = ref.watch(counterProvider);
    return Column(children: [
      Text('Count: $count'),
      ElevatedButton(
        onPressed: () => ref.read(counterProvider.notifier).state++,
        child: const Text('Increment'),
      ),
    ]);
  }
}
```

---

## Appendix D: Async in Flutter

```dart
// FutureBuilder — for one-time async operations
FutureBuilder<List<User>>(
  future: fetchUsers(),
  builder: (context, snapshot) {
    if (snapshot.connectionState == ConnectionState.waiting) {
      return const CircularProgressIndicator();
    }
    if (snapshot.hasError) {
      return Text('Error: ${snapshot.error}');
    }
    final users = snapshot.data!;
    return ListView.builder(
      itemCount: users.length,
      itemBuilder: (ctx, i) => Text(users[i].name),
    );
  },
)

// StreamBuilder — for continuous/live data
StreamBuilder<int>(
  stream: countStream(),
  builder: (context, snapshot) {
    if (!snapshot.hasData) return const CircularProgressIndicator();
    return Text('Value: ${snapshot.data}');
  },
)
```

---

## Appendix E: Useful Flutter Commands

```bash
# Check Flutter installation
flutter doctor

# Get dependencies
flutter pub get

# Add a package
flutter pub add provider

# Run on connected device
flutter run

# Run on specific device
flutter run -d chrome        # web
flutter run -d emulator-5554 # Android emulator
flutter run -d "iPhone 15"   # iOS simulator

# Hot reload (press 'r' while running in debug mode)
# Hot restart (press 'R' while running in debug mode)

# Build
flutter build apk               # Android APK
flutter build appbundle         # Android App Bundle (Play Store)
flutter build ios               # iOS (macOS only)
flutter build web               # Web app
flutter build macos             # macOS desktop

# Analyze code
flutter analyze

# Run tests
flutter test
flutter test test/widget_test.dart

# Upgrade Flutter
flutter upgrade
flutter channel stable && flutter upgrade
```

---

## Appendix F: Glossary

**Widget**
The fundamental building block of Flutter UIs. Everything is a widget — text, buttons, padding, layouts, and even the app itself. Widgets describe what the UI should look like; Flutter renders them on the GPU.

**StatelessWidget**
A widget with no mutable state. Once built, it doesn't change. Use for purely presentational widgets driven entirely by their properties (like `Text` or `Icon`).

**StatefulWidget**
A widget paired with a `State` object that can call `setState()` to trigger rebuilds. Use when the widget has interactive state that changes over time.

**BuildContext**
An object that represents the widget's location in the widget tree. Used to look up ancestors (like `Theme.of(context)`, `Provider.of<T>(context)`).

**Widget Tree / Element Tree / Render Tree**
Flutter uses three trees internally. The widget tree is what you write (lightweight configurations). The element tree manages lifecycle. The render tree handles actual painting. Understanding this explains why Flutter is fast.

**Hot Reload**
Injects updated code into the running app without losing state. Works for UI changes. Press `r` during `flutter run`.

**Pub / pub.dev**
Flutter's package manager. Packages are declared in `pubspec.yaml`. `pub.dev` is the package registry.

**Material / Cupertino**
Flutter ships with two design system libraries: Material Design (Google/Android style) and Cupertino (iOS style). Most apps use Material.

---

## Appendix G: Resources

- [Flutter Docs](https://docs.flutter.dev/) — official documentation
- [pub.dev](https://pub.dev/) — Flutter package registry
- [Flutter Widget Catalog](https://docs.flutter.dev/ui/widgets) — every built-in widget
- [Flutter Cookbook](https://docs.flutter.dev/cookbook) — practical recipes
- [Riverpod Docs](https://riverpod.dev/) — state management
- [GoRouter Docs](https://pub.dev/packages/go_router) — routing package
