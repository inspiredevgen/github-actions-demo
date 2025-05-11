# Github Actions Demo

# Qu'est-ce que GitHub Actions ?

GitHub Actions est une puissante plateforme d'automatisation directement intégrée à GitHub. Elle vous permet d'automatiser des tâches au sein de votre flux de travail de développement logiciel, directement dans votre dépôt. Considérez cela comme une manière de configurer des processus automatisés qui s'exécutent en réponse à des événements dans votre dépôt GitHub.

Voici une explication détaillée de ce que c'est et de ses aspects clés :

## Concepts Fondamentaux :

- **Workflows (Flux de travail) :** Ce sont des processus automatisés configurables définis dans des fichiers YAML. Un workflow peut comporter un ou plusieurs jobs et peut être déclenché par des événements tels que des _pushes_ de code, des _pull requests_, des horaires planifiés ou des déclenchements manuels. Les fichiers de workflow sont généralement stockés dans le répertoire `.github/workflows` de votre dépôt.
- **Événements (Events) :** Ce sont des activités spécifiques dans votre dépôt qui déclenchent l'exécution d'un workflow. Les exemples incluent le _push_ de code, la création d'une _pull request_, l'ouverture d'un _issue_ ou une nouvelle publication. Vous pouvez également déclencher des workflows selon un calendrier ou manuellement.
- **Jobs (Tâches) :** Un job est un ensemble d'étapes exécutées sur un _runner_ (un serveur). Les workflows peuvent avoir plusieurs jobs qui s'exécutent séquentiellement ou en parallèle. Chaque job s'exécute dans un environnement isolé.
- **Steps (Étapes) :** Une étape est une tâche individuelle au sein d'un job. Elle peut exécuter un script shell ou exécuter une **action**.
- **Actions :** Ce sont des unités d'automatisation réutilisables. Ce sont des paquets de code pré-construits qui effectuent des tâches spécifiques, ce qui facilite l'automatisation de workflows complexes sans écrire beaucoup de code à partir de zéro. Vous pouvez trouver des actions sur le [GitHub Marketplace](https://github.com/marketplace?type=actions), ou vous pouvez créer les vôtres.
- **Runners (Exécuteurs) :** Ce sont des serveurs qui exécutent vos workflows. GitHub fournit des _runners_ hébergés (avec des environnements Linux, macOS et Windows), ou vous pouvez utiliser des _runners_ auto-hébergés dans votre propre infrastructure.

## Fonctionnalités Clés de GitHub Actions :

- **Automatisation des Workflows :** Automatisez diverses étapes de votre cycle de vie de développement logiciel, y compris l'intégration continue (CI), la livraison continue (CD), les tests et le déploiement.
- **Déclencheurs Basés sur les Événements :** Les workflows peuvent être déclenchés par un large éventail d'événements GitHub, permettant une automatisation basée sur l'activité de votre dépôt.
- **Actions Réutilisables :** Tirez parti d'un vaste écosystème d'actions pré-construites sur le GitHub Marketplace ou créez vos propres actions personnalisées pour simplifier vos workflows.
- **Intégration avec l'Écosystème GitHub :** S'intègre de manière transparente avec d'autres fonctionnalités de GitHub telles que les _pull requests_, les _issues_ et les packages.
- **Large Prise en Charge des Langages :** Prend en charge divers langages de programmation tels que Node.js, Python, Java, Ruby, PHP, Go, Rust et .NET.
- **Runners Hébergés :** GitHub fournit des machines virtuelles avec des logiciels préinstallés pour divers systèmes d'exploitation, vous n'avez donc pas besoin de gérer votre propre infrastructure.
- **Runners Auto-Hébergés :** Offre la flexibilité d'utiliser vos propres serveurs pour plus de contrôle sur l'environnement et le matériel.
- **Gestion des Secrets :** Stockez et gérez en toute sécurité les informations sensibles telles que les clés API et les informations d'identification.
- **Constructions en Matrice :** Exécutez des jobs sur plusieurs systèmes d'exploitation et versions d'exécution simultanément pour gagner du temps.
- **Journaux en Direct :** Surveillez la progression de vos exécutions de workflow en temps réel grâce à des journaux détaillés.

## Comment Utiliser GitHub Actions :

1.  **Créer un Fichier de Workflow :** Dans votre dépôt, créez un répertoire nommé `.github/workflows`. À l'intérieur de ce répertoire, créez un fichier YAML (par exemple, `main.yml`) pour définir votre workflow.
2.  **Définir les Détails du Workflow :** Dans le fichier YAML, spécifiez le `name` (nom) de votre workflow, l'événement `on` (sur) qui le déclenche et les `jobs` (tâches) qu'il exécutera.
3.  **Configurer les Jobs :** Pour chaque job, définissez son `name` (nom) et l'environnement `runs-on` (s'exécute sur) (par exemple, `ubuntu-latest`). Ensuite, spécifiez la séquence des `steps` (étapes) à exécuter.
4.  **Utiliser des Actions et des Scripts :** Dans les `steps`, vous pouvez utiliser des actions pré-construites (en utilisant le mot-clé `uses`) ou exécuter des scripts shell (en utilisant le mot-clé `run`) pour effectuer des tâches.
5.  **Commit et Push :** Committez votre fichier de workflow dans votre dépôt. GitHub Actions reconnaîtra automatiquement le fichier et exécutera le workflow lorsque l'événement défini se produira.
6.  **Surveiller les Exécutions de Workflow :** Vous pouvez afficher l'état et les journaux de vos exécutions de workflow dans l'onglet "Actions" de votre dépôt sur GitHub.

GitHub Actions est un outil polyvalent qui peut considérablement améliorer votre flux de travail de développement en automatisant les tâches répétitives, en assurant la qualité du code grâce à des tests automatisés et en rationalisant votre processus de déploiement.
