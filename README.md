# libvirt-compose 🚀

**Modern, Declarative VM Orchestration for Libvirt.**

`libvirt-compose` is a lightweight Python tool designed to bring a "Compose-style" experience to KVM/Libvirt. It replaces complex XML configurations and brittle Ruby scripts with simple, scalable YAML definitions.

---

## ✨ Features

*   **Declarative Infrastructure:** Define your environment in `libvirt-compose.yaml`.
*   **Massive Scaling:** Use the `count` attribute to spawn dozens of identical nodes instantly.
*   **Fast Provisioning:** Leverages QCOW2 backing files for rapid "Gold Image" cloning.
*   **Modern Python Tooling:** Built using the `src` layout and managed by `uv` for maximum performance and reliability.

---