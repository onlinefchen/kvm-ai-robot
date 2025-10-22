# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 08:33:52

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 285
- **总 Thread 数**: 27
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 24 threads (266 邮件)
- **RFC**: 1 threads (10 邮件)
- **Other**: 2 threads (9 邮件)

---

## 📌 PATCH

共 24 个 thread

---

### Thread 1: [PATCH hyperv-next v5 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 50 | **👥 参与者**: 8 | **📅 开始时间**: Fri,  7 Mar 2025 14:02:52 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 ARM64 架构下的 Hyper-V 支持虚拟信任级别（VTL）引导的补丁集。原始补丁集包含 11 个补丁，旨在使 Hyper-V 代码能够在 ARM64 上以 VTL 模式启动，VTL 是虚拟安全模式的一部分。

在历史讨论中，Roman Kisel 提出了多个补丁，主要包括使用 SMCCC 检测 Hypervisor 存在、为 ARM64 启用 VTL 模式、提供架构中立的 VTL 检测实现等。这些补丁的目标是确保 ARM64 客户端能够在 VTL 模式下正常运行，并且对现有的 x86 代码进行必要的调整。

本周的新讨论中，参与者们对补丁集的具体实现进行了深入的讨论和反馈。Wei Liu 提出了对 VTL 检测一致性的关注，Krzysztof Kozlowski 对设备树绑定的描述提出了质疑，认为缺少必要的解释。Tianyu Lan 则询问了如何通过设备树找到 VMBus 根设备。Roman Kisel 对各项反馈表示感谢，并承诺将进一步改进补丁的描述和实现。

总体来看，本周的讨论集中在补丁的细节和实现一致性上，参与者们积极交流，推动补丁集的完善。

#### 📝 邮件列表

1. **[03-07 14:02]** [PATCH hyperv-next v5 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[03-07 14:02]** [PATCH hyperv-next v5 01/11] arm64: kvm, smccc: Introduce and use API for detectting hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
3. **[03-07 14:02]** [PATCH hyperv-next v5 02/11] arm64: hyperv: Use SMCCC to detect hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
4. **[03-07 14:02]** [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
5. **[03-07 14:02]** [PATCH hyperv-next v5 04/11] Drivers: hv: Provide arch-neutral implementation of get_vtl()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
6. **[03-07 14:02]** [PATCH hyperv-next v5 05/11] arm64: hyperv: Initialize the Virtual Trust Level field
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[03-07 14:02]** [PATCH hyperv-next v5 06/11] arm64, x86: hyperv: Report the VTL the system boots in
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
8. **[03-07 14:02]** [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add interrupts and DMA coherence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
9. **[03-07 14:03]** [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ number from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
10. **[03-07 14:03]** [PATCH hyperv-next v5 09/11] Drivers: hv: vmbus: Introduce hv_get_vmbus_root_device()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
11. **[03-07 14:03]** [PATCH hyperv-next v5 10/11] ACPI: irq: Introduce acpi_get_gsi_dispatcher()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
12. **[03-07 14:03]** [PATCH hyperv-next v5 11/11] PCI: hv: Get vPCI MSI IRQ domain from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
13. **[03-08 22:05]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Arnd Bergmann <arnd@arndb.de>
14. **[03-08 22:11]** Re: [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ number from
 DeviceTree
   - 发件人: Arnd Bergmann <arnd@arndb.de>
15. **[03-10 00:31]** Re: [PATCH hyperv-next v5 06/11] arm64, x86: hyperv: Report the VTL
 the system boots in
   - 发件人: Wei Liu <wei.liu@kernel.org>
16. **[03-10 10:28]** Re: [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add
 interrupts and DMA coherence
   - 发件人: Krzysztof Kozlowski <krzk@kernel.org>
17. **[03-10 21:41]** Re: [PATCH hyperv-next v5 09/11] Drivers: hv: vmbus: Introduce hv_get_vmbus_root_device()
   - 发件人: Tianyu Lan <ltykernel@gmail.com>
18. **[03-10 21:44]** Re: [PATCH hyperv-next v5 04/11] Drivers: hv: Provide arch-neutral
 implementation of get_vtl()
   - 发件人: Tianyu Lan <ltykernel@gmail.com>
19. **[03-10 11:41]** Re: [PATCH hyperv-next v5 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
20. **[03-10 09:42]** Re: [PATCH hyperv-next v5 06/11] arm64, x86: hyperv: Report the VTL
 the system boots in
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
21. **[03-10 16:53]** Re: [PATCH hyperv-next v5 06/11] arm64, x86: hyperv: Report the VTL
 the system boots in
   - 发件人: Wei Liu <wei.liu@kernel.org>
22. **[03-10 10:05]** Re: [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add
 interrupts and DMA coherence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
23. **[03-10 10:09]** Re: [PATCH hyperv-next v5 09/11] Drivers: hv: vmbus: Introduce
 hv_get_vmbus_root_device()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
24. **[03-10 10:15]** Re: [PATCH hyperv-next v5 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
25. **[03-10 10:20]** Re: [PATCH hyperv-next v5 06/11] arm64, x86: hyperv: Report the VTL
 the system boots in
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
26. **[03-10 10:35]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
27. **[03-10 10:36]** Re: [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ
 number from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
28. **[03-10 18:40]** Re: [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add
 interrupts and DMA coherence
   - 发件人: Krzysztof Kozlowski <krzk@kernel.org>
29. **[03-10 11:07]** Re: [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add
 interrupts and DMA coherence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
30. **[03-10 21:01]** RE: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Michael Kelley <mhklinux@outlook.com>
31. **[03-10 21:16]** RE: [PATCH hyperv-next v5 01/11] arm64: kvm, smccc: Introduce and use
 API for detectting hypervisor presence
   - 发件人: Michael Kelley <mhklinux@outlook.com>
32. **[03-10 22:17]** Re: [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add
 interrupts and DMA coherence
   - 发件人: Krzysztof Kozlowski <krzk@kernel.org>
33. **[03-10 21:17]** RE: [PATCH hyperv-next v5 02/11] arm64: hyperv: Use SMCCC to detect
 hypervisor presence
   - 发件人: Michael Kelley <mhklinux@outlook.com>
34. **[03-10 22:20]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Arnd Bergmann <arnd@arndb.de>
35. **[03-10 14:51]** Re: [PATCH hyperv-next v5 07/11] dt-bindings: microsoft,vmbus: Add
 interrupts and DMA coherence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
36. **[03-10 14:54]** Re: [PATCH hyperv-next v5 01/11] arm64: kvm, smccc: Introduce and use
 API for detectting hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
37. **[03-10 22:18]** RE: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Michael Kelley <mhklinux@outlook.com>
38. **[03-10 23:07]** RE: [PATCH hyperv-next v5 05/11] arm64: hyperv: Initialize the
 Virtual Trust Level field
   - 发件人: Michael Kelley <mhklinux@outlook.com>
39. **[03-10 23:09]** RE: [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ
 number from DeviceTree
   - 发件人: Michael Kelley <mhklinux@outlook.com>
40. **[03-10 23:12]** RE: [PATCH hyperv-next v5 09/11] Drivers: hv: vmbus: Introduce
 hv_get_vmbus_root_device()
   - 发件人: Michael Kelley <mhklinux@outlook.com>
41. **[03-10 23:26]** RE: [PATCH hyperv-next v5 10/11] ACPI: irq: Introduce
 acpi_get_gsi_dispatcher()
   - 发件人: Michael Kelley <mhklinux@outlook.com>
42. **[03-10 23:42]** RE: [PATCH hyperv-next v5 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Michael Kelley <mhklinux@outlook.com>
43. **[03-12 11:33]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
44. **[03-12 21:25]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Arnd Bergmann <arnd@arndb.de>
45. **[03-12 20:31]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Wei Liu <wei.liu@kernel.org>
46. **[03-12 14:21]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
47. **[03-12 14:30]** Re: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
48. **[03-13 05:10]** RE: [PATCH hyperv-next v5 03/11] Drivers: hv: Enable VTL mode for
 arm64
   - 发件人: Michael Kelley <mhklinux@outlook.com>
49. **[03-13 13:44]** Re: [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ
 number from DeviceTree
   - 发件人: Rob Herring <robh@kernel.org>
50. **[03-13 11:46]** Re: [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ
 number from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>

---

### Thread 2: [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM

**📧 邮件数**: 27 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 26 Feb 2025 21:55:16 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁，主要集中在 HCRX_EL2 的初始化和其他陷阱的处理。

1. **原始补丁内容**：Fuad Tabba 提出的补丁系列（PATCH v2 0/4）旨在修复 pKVM 中 HCRX_EL2 的初始化问题，并将相关逻辑分离为独立函数，以便在受保护和非受保护模式下共享代码。补丁还涉及到 FF-A（Firmware Framework for Arm）缓冲区的初始化和管理。

2. **之前讨论要点**：在历史讨论中，参与者们探讨了补丁的实现细节，包括如何处理 vcpu 的创建和初始化，以及在 FF-A 调用中的版本协商问题。Will Deacon 提出了一些关于并发性和内存共享的担忧，尤其是在不同版本之间的兼容性。

3. **本周的新讨论与进展**：本周的讨论集中在对补丁的进一步修正上，尤其是关于 WRITE_ONCE() 的使用问题。Will Deacon 建议将其从补丁中移除，并确认了在处理 RX 缓冲区所有权释放时的正确行为。此外，参与者们讨论了在未来支持 guest-FFA 时的版本协商责任，认为目前的设计不需要复杂的版本管理。

总体来说，邮件线程展示了对 KVM arm64 的重要修复和改进，参与者们积极讨论并推动补丁的完善。

#### 📝 邮件列表

1. **[02-26 21:55]** [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-26 21:55]** [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-27 18:17]** [PATCH v2 0/4] KVM: arm64: Separate the hyp FF-A buffers init from
 the host
   - 发件人: Sebastian Ene <sebastianene@google.com>
4. **[02-27 18:17]** [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
5. **[02-27 18:17]** [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx buffer
 to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
6. **[02-28 19:44]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Quentin Perret <qperret@google.com>
7. **[03-03 07:57]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[03-03 19:18]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>
9. **[03-03 19:21]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[03-03 21:49]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>
11. **[03-03 23:43]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
12. **[03-04 00:53]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
13. **[03-04 01:56]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
14. **[03-04 12:33]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[03-04 17:38]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
16. **[03-05 00:38]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
17. **[03-05 00:45]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Will Deacon <will@kernel.org>
18. **[03-05 09:41]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
19. **[03-05 18:36]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
20. **[03-05 19:34]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Will Deacon <will@kernel.org>
21. **[03-06 09:40]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
22. **[03-12 15:29]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>
23. **[03-12 15:31]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
24. **[03-13 12:04]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
25. **[03-13 12:15]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Will Deacon <will@kernel.org>
26. **[03-13 14:00]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
27. **[03-14 11:14]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 3: [PATCH v2 00/23] KVM: arm64: Revamp Fine Grained Trap handling

**📧 邮件数**: 24 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 10 Mar 2025 12:24:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 ARM64 架构下的细粒度陷阱（Fine Grained Trap, FGT）处理的改进。Marc Zyngier 提出的补丁系列（PATCH v2 00/23）旨在重构 FGT 的处理方式，特别是 RES0 位的管理，以提高系统的未来兼容性和稳定性。

在历史讨论中，Marc 提到目前的 FGT 处理方式存在潜在问题，尤其是 RES0 位的行为并不总是与 KVM 的启用状态同步，可能导致意外行为。因此，补丁的主要目标是重新引入 KVM 对 RES0 掩码的视图，确保在处理 FGT 时能够安全地忽略某些特性。

本周的新讨论中，Marc 提出了多个具体的补丁，涵盖了 FGT 掩码的计算、FGT 注册表的配置以及与特性映射的集成。这些补丁包括：
1. 引入新的 FGT 特性映射表，以便于管理和验证 RES0 位。
2. 通过计算 FGT 掩码来简化 KVM 对 FGT 注册的处理。
3. 增强 HCRX_EL2 和 HCR_EL2 的特性映射，以确保它们的 RES0 状态与相应特性一致。

总体而言，这些改进旨在减少复杂性，提高代码的可维护性，并确保 KVM 在未来的 ARM64 架构更新中能够更好地适应新特性。

#### 📝 邮件列表

1. **[03-10 12:24]** [PATCH v2 00/23] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-10 12:24]** [PATCH v2 01/23] arm64: sysreg: Add ID_AA64ISAR1_EL1.LS64 encoding for FEAT_LS64WB
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-10 12:24]** [PATCH v2 02/23] arm64: sysreg: Update ID_AA64MMFR4_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-10 12:24]** [PATCH v2 03/23] arm64: sysreg: Add layout for HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[03-10 12:24]** [PATCH v2 04/23] arm64: Add syndrome information for trapped LD64B/ST64B{,V,V0}
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-10 12:24]** [PATCH v2 05/23] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[03-10 12:24]** [PATCH v2 06/23] KVM: arm64: Restrict ACCDATA_EL1 undef to FEAT_ST64_ACCDATA being disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[03-10 12:24]** [PATCH v2 07/23] KVM: arm64: Don't treat HCRX_EL2 as a FGT register
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[03-10 12:24]** [PATCH v2 08/23] KVM: arm64: Plug FEAT_GCS handling
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[03-10 12:24]** [PATCH v2 09/23] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[03-10 12:24]** [PATCH v2 10/23] KVM: arm64: Add description of FGT bits leading to EC!=0x18
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-10 12:24]** [PATCH v2 11/23] KVM: arm64: Use computed masks as sanitisers for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[03-10 12:24]** [PATCH v2 12/23] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[03-10 12:24]** [PATCH v2 13/23] KVM: arm64: Propagate FGT masks to the nVHE hypervisor
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[03-10 12:24]** [PATCH v2 14/23] KVM: arm64: Use computed FGT masks to setup FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[03-10 12:24]** [PATCH v2 15/23] KVM: arm64: Remove most hand-crafted masks for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[03-10 12:24]** [PATCH v2 16/23] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[03-10 12:24]** [PATCH v2 17/23] KVM: arm64: Handle PSB CSYNC traps
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[03-10 12:25]** [PATCH v2 18/23] KVM: arm64: Switch to table-driven FGU configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[03-10 12:25]** [PATCH v2 19/23] KVM: arm64: Validate FGT register descriptions against RES0 masks
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[03-10 12:25]** [PATCH v2 20/23] KVM: arm64: Use FGT feature maps to drive RES0 bits
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[03-10 12:25]** [PATCH v2 21/23] KVM: arm64: Allow kvm_has_feat() to take variable arguments
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[03-10 12:25]** [PATCH v2 22/23] KVM: arm64: Use HCRX_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[03-10 12:25]** [PATCH v2 23/23] KVM: arm64: Use HCR_EL2 feature map to drive fixed-value bits
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 4: [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware

**📧 邮件数**: 20 | **👥 参与者**: 4 | **📅 开始时间**: Wed,  5 Mar 2025 12:26:27 -0800

#### 🤖 AI 总结

本邮件线程讨论了关于在Apple硬件上实现KVM（Kernel-based Virtual Machine）对ARM64架构的PMUv3（性能监控单元v3）支持的补丁系列。

1. **原始补丁内容**：补丁系列的主题为“[PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware”，主要目的是在Apple硬件上实现对PMUv3的支持，补丁中包括了对事件选择和过滤配置的重构，以及支持主机和客机事件过滤的功能。

2. **历史讨论要点**：在之前的讨论中，补丁经过了几轮修改，主要针对Marc Zyngier的反馈进行了调整。补丁的结构和顺序被重新组织，以确保更好的可读性和功能实现。此外，补丁中还禁止了无效的PMUv3事件映射。

3. **本周的新讨论和进展**：本周的讨论中，Marc Zyngier对补丁的整体外观表示满意，并给予了“Reviewed-by”标记。Cornelia Huck则提交了多个补丁，涉及ID寄存器的重构和存储功能，进一步完善了对ARM64架构的支持。邮件中还提到了一些生成系统寄存器定义的脚本，虽然Marc表示不认为这些脚本会被合并到内核中，但Cornelia表示会单独维护。最后，Oliver Upton确认已将补丁应用于下一个版本。

总体来看，本次讨论集中在对KVM在Apple硬件上支持ARM64 PMUv3的实现细节上，涉及补丁的修改、审查和未来的维护计划。

#### 📝 邮件列表

1. **[03-05 12:26]** [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[03-10 13:13]** Re: [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-11 17:28]** [PATCH v3 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[03-11 17:28]** [PATCH v3 01/14] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[03-11 17:28]** [PATCH v3 02/14] arm/kvm: add accessors for storing host features into idregs
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[03-11 17:28]** [PATCH v3 03/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[03-11 17:28]** [PATCH v3 04/14] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[03-11 17:28]** [PATCH v3 05/14] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[03-11 17:28]** [PATCH v3 06/14] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[03-11 17:28]** [PATCH v3 07/14] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[03-11 17:28]** [PATCH v3 08/14] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[03-11 17:28]** [PATCH v3 09/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[03-11 17:28]** [PATCH v3 10/14] arm/cpu: Store id_pfr0/1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[03-11 17:28]** [PATCH v3 11/14] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[03-11 17:28]** [PATCH v3 12/14] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
16. **[03-11 17:28]** [PATCH v3 13/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
17. **[03-11 17:28]** [PATCH v3 14/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>
18. **[03-11 10:40]** Re: [PATCH v3 02/14] arm/kvm: add accessors for storing host features
 into idregs
   - 发件人: Richard Henderson <richard.henderson@linaro.org>
19. **[03-11 18:12]** Re: [PATCH v3 00/14] arm: rework id register storage
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[03-11 16:44]** Re: [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 5: [PATCH 6.13 0/8] KVM: arm64: Backport of SVE fixes to v6.13

**📧 邮件数**: 17 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 12 Mar 2025 23:49:08 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构上的一系列补丁，主要集中在 SVE（可扩展向量扩展）和 FPSIMD（浮点 SIMD）状态的处理上。

1. **原始补丁内容**：补丁系列旨在将 Mark Rutland 提出的 SVE 和 KVM 交互的修复回移植到 v6.13 版本。这些补丁包括对 cptr_el2 陷阱的计算、无条件保存和刷新主机的 FPSIMD/SVE/SME 状态、移除非保护 KVM 的主机 FPSIMD 保存、以及重构退出处理程序等。

2. **之前讨论要点**：在历史讨论中，参与者们探讨了如何处理主机和虚拟机之间的状态保存问题，尤其是在 SVE 状态的管理上。之前的实现存在一些问题，比如主机的 SVE 状态可能会在不一致的情况下被丢弃，导致 QEMU 崩溃等问题。

3. **本周新讨论与进展**：本周的讨论中，所有补丁都已被添加到 6.13-stable 树中。补丁包括：
   - 计算 cptr_el2 陷阱的补丁；
   - 无条件保存和刷新主机 FPSIMD/SVE/SME 状态的补丁；
   - 移除非保护 KVM 的主机 FPSIMD 保存的补丁；
   - 移除 VHE 模式下对 CPACR_EL1.ZEN 和 CPACR_EL1.SMEN 的恢复逻辑的补丁；
   - 退出处理程序的重构补丁。

这些补丁的合并旨在提高 KVM 的稳定性和性能，确保主机和虚拟机之间的状态管理更加高效。

#### 📝 邮件列表

1. **[03-12 23:49]** [PATCH 6.13 0/8] KVM: arm64: Backport of SVE fixes to v6.13
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[03-12 23:49]** [PATCH 6.13 1/8] KVM: arm64: Calculate cptr_el2 traps on
 activating traps
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[03-12 23:49]** [PATCH 6.13 2/8] KVM: arm64: Unconditionally save+flush host
 FPSIMD/SVE/SME state
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[03-12 23:49]** [PATCH 6.13 3/8] KVM: arm64: Remove host FPSIMD saving for
 non-protected KVM
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[03-12 23:49]** [PATCH 6.13 4/8] KVM: arm64: Remove VHE host restore of
 CPACR_EL1.ZEN
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[03-12 23:49]** [PATCH 6.13 5/8] KVM: arm64: Remove VHE host restore of
 CPACR_EL1.SMEN
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[03-12 23:49]** [PATCH 6.13 6/8] KVM: arm64: Refactor exit handlers
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[03-12 23:49]** [PATCH 6.13 7/8] KVM: arm64: Mark some header functions as inline
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[03-12 23:49]** [PATCH 6.13 8/8] KVM: arm64: Eagerly switch ZCR_EL{1,2}
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[03-13 17:09]** Patch "KVM: arm64: Calculate cptr_el2 traps on activating traps" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
11. **[03-13 17:09]** Patch "KVM: arm64: Eagerly switch ZCR_EL{1,2}" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
12. **[03-13 17:09]** Patch "KVM: arm64: Mark some header functions as inline" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
13. **[03-13 17:09]** Patch "KVM: arm64: Unconditionally save+flush host FPSIMD/SVE/SME state" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
14. **[03-13 17:09]** Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.ZEN" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
15. **[03-13 17:09]** Patch "KVM: arm64: Remove VHE host restore of CPACR_EL1.SMEN" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
16. **[03-13 17:09]** Patch "KVM: arm64: Remove host FPSIMD saving for non-protected KVM" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
17. **[03-13 17:09]** Patch "KVM: arm64: Refactor exit handlers" has been added to the 6.13-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 6: [PATCH hyperv-next v6 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 16 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 14 Mar 2025 17:19:20 -0700

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH hyperv-next v6 00/11] arm64: hyperv: 支持虚拟信任级别启动”。该补丁集旨在使 Hyper-V 代码能够在 ARM64 架构下支持虚拟信任级别（VTL）启动，相关文档可参考 Microsoft 的 TLFS 规范。

在历史讨论中，补丁的前几个版本（V1-V5）主要集中在如何检测 Hyper-V 超级管理程序的存在，最初依赖于 ACPI 进行检测。随着讨论的深入，补丁逐步引入了 SMCCC（安全监控调用约定）来实现更通用的检测方法，并对代码进行了多次重构和优化。

在本周的新讨论中，Roman Kisel 提出了补丁的最新版本（V6），并详细介绍了补丁的具体内容和改进，包括：
1. 引入了用于检测 Hyper-V 存在性的 API。
2. 更新了 Kconfig 配置，使 ARM64 客户端能够在没有 ACPI 的情况下启用 VTL 模式。
3. 通过 DeviceTree 获取 VMBus 的中断配置，以支持在 VTL 模式下的操作。
4. 增加了对 VTL 的初始化和报告功能，确保在启动时能够正确识别和使用 VTL。

此外，参与者对补丁的各个方面进行了审查和反馈，部分补丁得到了认可（Acked），并提出了代码风格和文档描述的改进建议。整体来看，本周的讨论推动了补丁的进一步完善，朝着实现 ARM64 下的 VTL 启动目标迈出了重要一步。

#### 📝 邮件列表

1. **[03-14 17:19]** [PATCH hyperv-next v6 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[03-14 17:19]** [PATCH hyperv-next v6 01/11] arm64: kvm, smccc: Introduce and use API for detecting hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
3. **[03-14 17:19]** [PATCH hyperv-next v6 02/11] arm64: hyperv: Use SMCCC to detect hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
4. **[03-14 17:19]** [PATCH hyperv-next v6 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
5. **[03-14 17:19]** [PATCH hyperv-next v6 04/11] Drivers: hv: Provide arch-neutral implementation of get_vtl()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
6. **[03-14 17:19]** [PATCH hyperv-next v6 05/11] arm64: hyperv: Initialize the Virtual Trust Level field
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[03-14 17:19]** [PATCH hyperv-next v6 06/11] arm64, x86: hyperv: Report the VTL the system boots in
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
8. **[03-14 17:19]** [PATCH hyperv-next v6 07/11] dt-bindings: microsoft,vmbus: Add interrupt and DMA coherence properties
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
9. **[03-14 17:19]** [PATCH hyperv-next v6 08/11] Drivers: hv: vmbus: Get the IRQ number from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
10. **[03-14 17:19]** [PATCH hyperv-next v6 09/11] Drivers: hv: vmbus: Introduce hv_get_vmbus_root_device()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
11. **[03-14 17:19]** [PATCH hyperv-next v6 10/11] ACPI: irq: Introduce  acpi_get_gsi_dispatcher()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
12. **[03-14 17:19]** [PATCH hyperv-next v6 11/11] PCI: hv: Get vPCI MSI IRQ domain from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
13. **[03-14 17:27]** Re: [PATCH hyperv-next v6 01/11] arm64: kvm, smccc: Introduce and use
 API for detecting hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
14. **[03-15 14:12]** Re: [PATCH hyperv-next v6 01/11] arm64: kvm, smccc: Introduce and use API for
 detecting hypervisor presence
   - 发件人: Arnd Bergmann <arnd@arndb.de>
15. **[03-15 13:49]** Re: [PATCH hyperv-next v6 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Bjorn Helgaas <helgaas@kernel.org>
16. **[03-16 18:36]** Re: [PATCH hyperv-next v6 07/11] dt-bindings: microsoft,vmbus: Add
 interrupt and DMA coherence properties
   - 发件人: Krzysztof Kozlowski <krzk@kernel.org>

---

### Thread 7: [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Feb 2025 00:33:04 +0000

#### 🤖 AI 总结

本邮件线程讨论了将 pKVM 所有权状态迁移到 hyp_vmemmap 的一系列补丁（PATCH 0/6）。该补丁的主要目的是提高超管状态的查找效率，避免了对 hyp 阶段 1 页表的遍历，同时解耦了超管状态与线性映射范围内的映射关系，为未来的功能扩展（如 hyp 跟踪）提供了便利。

在历史讨论中，Quentin Perret 提出了补丁的背景和好处，强调了通过将超管状态移至 hyp_vmemmap 可以简化现有代码并提高安全性。Vincent Donnefort 提出了一些关于 SHARED_OWNED 和 SHARED_BORROWED 状态是否仍然相关的疑问。

在本周的新讨论中，Quentin 和 Marc Zyngier 进一步探讨了补丁的实现细节，确认了超管状态现在是基于物理地址（PA）进行跟踪，而不是虚拟地址（VA）。Marc 还提到，虽然目前存在两种状态（每个映射的状态和每页的状态），但这种设计是合理的，未来可能需要对相关文档进行澄清。最终，Marc 对补丁进行了审核并表示支持。整体来看，讨论围绕补丁的实现细节、潜在的清理工作和未来的扩展方向展开，进展顺利。

#### 📝 邮件列表

1. **[02-27 00:33]** [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-27 00:33]** [PATCH 2/6] KVM: arm64: Use 0b11 for encoding PKVM_NOPAGE
   - 发件人: Quentin Perret <qperret@google.com>
3. **[02-27 00:33]** [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
4. **[03-03 09:47]** Re: [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[03-13 19:13]** Re: [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
6. **[03-14 11:07]** Re: [PATCH 2/6] KVM: arm64: Use 0b11 for encoding PKVM_NOPAGE
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[03-14 11:31]** Re: [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[03-14 14:06]** Re: [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
9. **[03-14 14:13]** Re: [PATCH 2/6] KVM: arm64: Use 0b11 for encoding PKVM_NOPAGE
   - 发件人: Quentin Perret <qperret@google.com>
10. **[03-16 11:03]** Re: [PATCH 2/6] KVM: arm64: Use 0b11 for encoding PKVM_NOPAGE
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[03-16 11:08]** Re: [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-16 11:12]** Re: [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH 6.12 0/8] KVM: arm64: Backport of SVE fixes to v6.12

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 14 Mar 2025 00:35:12 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 SVE（Scalable Vector Extension）相关修复的补丁系列，主题为“[PATCH 6.12 0/8] KVM: arm64: Backport of SVE fixes to v6.12”。

**原始补丁/问题内容**：
补丁系列主要目的是将 Mark Rutland 提出的 SVE/KVM 交互的修复回溯到 v6.12 版本。这些修复涉及多个方面，包括对 FPSIMD/SVE/SME 状态的处理和异常处理逻辑的改进。

**之前讨论要点**：
在历史讨论中，参与者们关注了 KVM 在处理 SVE 状态时的复杂性，特别是在不同的虚拟化模式下（如 VHE 和 nVHE）对状态保存和恢复的影响。之前的实现存在一些问题，例如在非保护模式下不必要地保存主机的 FPSIMD 状态。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上。Mark Brown 提出了多个补丁，逐步移除冗余的状态保存逻辑，简化了 KVM 的状态管理。补丁中包括：
1. 移除非保护 KVM 的主机 FPSIMD 状态保存逻辑。
2. 改进了 ZCR_EL{1,2} 的切换逻辑，以确保在虚拟机与主机之间切换时能正确处理 SVE 状态。
3. 重构了退出处理程序，减少了代码重复。

此外，邮件中还涉及了对补丁的审查和确认，确保这些改动能够被顺利合并到主线中。整体来看，本周的讨论推动了补丁的完善和实施，旨在提高 KVM 在 arm64 架构下的性能和稳定性。

#### 📝 邮件列表

1. **[03-14 00:35]** [PATCH 6.12 0/8] KVM: arm64: Backport of SVE fixes to v6.12
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[03-14 00:35]** [PATCH 6.12 1/8] KVM: arm64: Calculate cptr_el2 traps on
 activating traps
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[03-14 00:35]** [PATCH 6.12 2/8] KVM: arm64: Unconditionally save+flush host
 FPSIMD/SVE/SME state
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[03-14 00:35]** [PATCH 6.12 3/8] KVM: arm64: Remove host FPSIMD saving for
 non-protected KVM
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[03-14 00:35]** [PATCH 6.12 4/8] KVM: arm64: Remove VHE host restore of
 CPACR_EL1.ZEN
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[03-14 00:35]** [PATCH 6.12 5/8] KVM: arm64: Remove VHE host restore of
 CPACR_EL1.SMEN
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[03-14 00:35]** [PATCH 6.12 6/8] KVM: arm64: Refactor exit handlers
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[03-14 00:35]** [PATCH 6.12 7/8] KVM: arm64: Mark some header functions as inline
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[03-14 00:35]** [PATCH 6.12 8/8] KVM: arm64: Eagerly switch ZCR_EL{1,2}
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[03-14 06:32]** Re: [PATCH 6.12 3/8] KVM: arm64: Remove host FPSIMD saving for
 non-protected KVM
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
11. **[03-14 14:40]** Re: [PATCH 6.12 3/8] KVM: arm64: Remove host FPSIMD saving for
 non-protected KVM
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[03-14 15:07]** Re: [PATCH 6.12 3/8] KVM: arm64: Remove host FPSIMD saving for
 non-protected KVM
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 9: [PATCH v1 0/5] Support the FEAT_HDBSS introduced in Armv9.5

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 11 Mar 2025 12:03:16 +0800

#### 🤖 AI 总结

本邮件讨论的主题是支持 ARMv9.5 引入的硬件脏状态跟踪结构（HDBSS）。该系列补丁旨在增强对翻译表描述符脏状态的跟踪，以降低实时迁移时的执行开销。

**原始补丁内容**：补丁系列包含五个部分，主要功能是添加 HDBSS 特性支持，包括相关寄存器信息、内存中断时设置 DBM 属性、通过 ioctl 启用/禁用 HDBSS 特性、处理 HDBSSF 事件以及控制 HDBSS 特性的配置。

**之前讨论要点**：历史讨论较少，主要集中在补丁的技术细节和实现方法上。补丁的目标是优化 KVM 的性能，特别是在虚拟机迁移时。

**本周新讨论进展**：本周的讨论主要集中在补丁的实现细节和潜在问题上。参与者对存储原始系统寄存器值在 vCPU 结构中的做法表示担忧，认为应将缓冲区基地址、大小和索引分开存储。此外，关于使用 DSB 指令的必要性、内存分配失败时的处理、以及如何在用户空间中正确反映这些变化等问题也引发了讨论。Marc Zyngier 和 Oliver Upton 提出了多项改进建议，强调需要更清晰的抽象和更合理的错误处理机制。

总体而言，尽管补丁的目标明确，但在实现细节上仍需进一步讨论和完善。

#### 📝 邮件列表

1. **[03-11 12:03]** [PATCH v1 0/5] Support the FEAT_HDBSS introduced in Armv9.5
   - 发件人: Zhenyu Ye <yezhenyu2@huawei.com>
2. **[03-11 12:03]** [PATCH v1 1/5] arm64/sysreg: add HDBSS related register information
   - 发件人: Zhenyu Ye <yezhenyu2@huawei.com>
3. **[03-11 12:03]** [PATCH v1 2/5] arm64/kvm: support set the DBM attr during memory abort
   - 发件人: Zhenyu Ye <yezhenyu2@huawei.com>
4. **[03-11 12:03]** [PATCH v1 3/5] arm64/kvm: using ioctl to enable/disable the HDBSS feature
   - 发件人: Zhenyu Ye <yezhenyu2@huawei.com>
5. **[03-11 12:03]** [PATCH v1 4/5] arm64/kvm: support to handle the HDBSSF event
   - 发件人: Zhenyu Ye <yezhenyu2@huawei.com>
6. **[03-11 12:03]** [PATCH v1 5/5] arm64/config: add config to control whether enable HDBSS feature
   - 发件人: Zhenyu Ye <yezhenyu2@huawei.com>
7. **[03-11 01:05]** Re: [PATCH v1 3/5] arm64/kvm: using ioctl to enable/disable the
 HDBSS feature
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[03-11 09:41]** Re: [PATCH v1 1/5] arm64/sysreg: add HDBSS related register information
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[03-11 09:47]** Re: [PATCH v1 2/5] arm64/kvm: support set the DBM attr during memory abort
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[03-11 09:53]** Re: [PATCH v1 5/5] arm64/config: add config to control whether enable HDBSS feature
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[03-11 09:59]** Re: [PATCH v1 3/5] arm64/kvm: using ioctl to enable/disable the HDBSS feature
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-11 10:34]** Re: [PATCH v1 4/5] arm64/kvm: support to handle the HDBSSF event
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH v3 0/6] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 12 Mar 2025 20:55:54 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的性能监控单元（PMU）相关的补丁系列，主要集中在修复 vPMC（虚拟性能监控计数器）寄存器的 SET_ONE_REG 操作。

1. **原始补丁内容**：补丁系列的目标是修复用户在第一次运行后对 vPMC 寄存器的修改，确保在调试 Windows 操作系统时，QEMU 不会因恢复虚拟机执行而破坏 PMU 状态。补丁还包括恢复过去对 PMU 寄存器的语义更改，以确保在 Firecracker、QEMU 和 crosvm 上正确迁移 PMU 状态。

2. **之前讨论要点**：补丁系列的 v2 版本中，针对用户空间寄存器写入和寄存器重置的处理进行了扩展，确保在用户修改寄存器时能够正确重新加载 PMU 配置。讨论中提到的关键问题是，早期的更改可能导致 KVM_SET_ONE_REG 的行为不符合预期，影响虚拟机的迁移。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的具体实现和改进上。Akihiko Odaki 提出了多个补丁，包括在用户修改寄存器时触发 PMU 重新加载，以及确保在设置 vPMC 寄存器时正确处理当前的性能事件。Oliver Upton 对某些补丁提出了建议，建议在 ioctl 实现中保留 PMU 检查，并建议将某些功能的调用顺序进行调整，以提升代码的一致性和可读性。

总体来看，本周的讨论推动了补丁的进一步完善，确保了在虚拟化环境中对 PMU 的正确管理和调试支持。

#### 📝 邮件列表

1. **[03-12 20:55]** [PATCH v3 0/6] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
2. **[03-12 20:55]** [PATCH v3 1/6] KVM: arm64: PMU: Set raw values from user to
 PM{C,I}NTEN{SET,CLR}, PMOVS{SET,CLR}
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
3. **[03-12 20:55]** [PATCH v3 2/6] KVM: arm64: PMU: Assume PMU presence in pmu-emul.c
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
4. **[03-12 20:55]** [PATCH v3 3/6] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
5. **[03-12 20:55]** [PATCH v3 4/6] KVM: arm64: PMU: Reload when user modifies
 registers
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
6. **[03-12 20:55]** [PATCH v3 5/6] KVM: arm64: PMU: Call kvm_pmu_handle_pmcr() after
 masking PMCNTENSET_EL0
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
7. **[03-12 20:56]** [PATCH v3 6/6] KVM: arm64: Reload PMCNTENSET_EL0
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
8. **[03-12 14:08]** Re: [PATCH v3 2/6] KVM: arm64: PMU: Assume PMU presence in pmu-emul.c
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[03-12 14:18]** Re: [PATCH v3 4/6] KVM: arm64: PMU: Reload when user modifies
 registers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[03-12 14:23]** Re: [PATCH v3 6/6] KVM: arm64: Reload PMCNTENSET_EL0
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 11: [PATCH v4 0/7] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 13 Mar 2025 15:57:41 +0900

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的性能监控单元（PMU）相关的补丁系列，主要目的是修复 vPMC（虚拟性能监控计数器）寄存器的 SET_ONE_REG 操作。

**原始问题及补丁内容**：
补丁系列的核心是修复在用户空间对 vPMC 寄存器进行修改时，KVM 需要正确更新 PMU 状态，以避免在调试 Windows 操作系统时出现问题。具体来说，补丁中包含的一个重要修改是确保在用户修改寄存器后，能够重新加载 PMU 配置，以保持寄存器状态的一致性。

**历史讨论要点**：
之前的讨论主要集中在如何处理用户空间对 PMU 寄存器的写入操作，以及这些操作如何影响虚拟机的迁移和性能监控。补丁系列的设计旨在恢复之前对寄存器的语义，并确保在不同的虚拟机监控器（如 QEMU 和 Firecracker）中能够正确处理 PMU 状态。

**本周新讨论及进展**：
本周的讨论中，Akihiko Odaki 提交了七个补丁，逐一解决了与 vPMC 寄存器相关的多个问题，包括如何在用户修改寄存器时触发 PMU 重新加载、修复 SET_ONE_REG 操作的行为等。此外，参与者 Oliver Upton 提出了补丁不适用于某些内核版本的问题，表明补丁的基础版本可能较旧，需进一步确认。

总的来说，本周的讨论推动了 PMU 相关补丁的完善，确保了在 ARM64 架构下的 KVM 能够更好地支持性能监控功能。

#### 📝 邮件列表

1. **[03-13 15:57]** [PATCH v4 0/7] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
2. **[03-13 15:57]** [PATCH v4 1/7] KVM: arm64: PMU: Set raw values from user to
 PM{C,I}NTEN{SET,CLR}, PMOVS{SET,CLR}
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
3. **[03-13 15:57]** [PATCH v4 2/7] KVM: arm64: PMU: Assume PMU presence in pmu-emul.c
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
4. **[03-13 15:57]** [PATCH v4 3/7] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
5. **[03-13 15:57]** [PATCH v4 4/7] KVM: arm64: PMU: Reload when user modifies
 registers
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
6. **[03-13 15:57]** [PATCH v4 5/7] KVM: arm64: PMU: Call kvm_pmu_handle_pmcr() after
 masking PMCNTENSET_EL0
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
7. **[03-13 15:57]** [PATCH v4 6/7] KVM: arm64: PMU: Reload PMCNTENSET_EL0
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
8. **[03-13 15:57]** [PATCH v4 7/7] KVM: arm64: PMU: Reload when resetting
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
9. **[03-14 01:10]** Re: [PATCH v4 0/7] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 12: [PATCH v3 0/3] Count pKVM stage-2 usage in secondary pagetable stat

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Mar 2025 11:34:08 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 pKVM 的补丁系列，旨在统计在使用 pKVM 时 stage-2 相关内存的使用情况，并在 `/proc/meminfo` 中的 `SecPageTables` 字段中显示该值。

**历史讨论**中，Vincent Donnefort 提出了三个补丁：
1. **补丁 1**：为 `kvm_hyp_memcache` 添加标志，以便在内存分配和释放时进行更好的管理。
2. **补丁 2**：为 stage-2 页表的拆除使用独立的内存缓存，以便更准确地统计内存使用。
3. **补丁 3**：对前两个补丁进行了相关修改和优化。

在之前的讨论中，参与者主要关注补丁中的一些实现细节和命名问题，尤其是如何更清晰地定义和管理 stage-2 页表的内存。

**本周新讨论**中，Marc Zyngier 对补丁 1 和补丁 2 提出了具体的疑问和建议，指出某些类型转换和命名可能存在多余或不清晰的地方。Vincent Donnefort 对这些反馈进行了回应，表示会进行相应的修改，并确认了补丁的改进方向。最终，Marc 对补丁表示认可，认为其已经得到了很好的改进。

总体来看，本周的讨论主要集中在补丁的细节优化上，参与者之间的互动促进了补丁的完善。

#### 📝 邮件列表

1. **[03-07 11:34]** [PATCH v3 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-07 11:34]** [PATCH v3 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-07 11:34]** [PATCH v3 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-12 08:38]** Re: [PATCH v3 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[03-12 08:59]** Re: [PATCH v3 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-13 09:13]** Re: [PATCH v3 2/3] KVM: arm64: Distinct pKVM teardown memcache for
 stage-2
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[03-13 09:16]** Re: [PATCH v3 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[03-13 09:31]** Re: [PATCH v3 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v5 0/5] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 15 Mar 2025 18:12:09 +0900

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下的 PMU（性能监控单元）相关问题的补丁集，主要集中在修复 `SET_ONE_REG` 对 vPMC（虚拟性能监控计数器）寄存器的处理。

1. **原始补丁内容**：补丁系列旨在修复 vPMC 寄存器在用户空间修改后状态不一致的问题，特别是在调试 Windows 操作系统时，QEMU 在恢复虚拟机执行时会尝试写回所有可见寄存器，可能会破坏 PMU 状态。补丁包括多个修复，确保在用户修改寄存器后能正确重新加载 PMU 状态。

2. **之前讨论要点**：历史讨论中提到，之前的实现对 vPMC 寄存器的处理存在语义上的不一致，导致在迁移过程中可能出现问题。补丁通过恢复寄存器的原始值来解决这一问题。

3. **本周新讨论与进展**：本周的讨论中，Akihiko Odaki 提出了五个补丁，分别修复了用户对 vPMC 寄存器的修改、假设 PMU 存在的函数、修复 `SET_ONE_REG` 的行为、以及在用户修改寄存器和重置时重新加载 PMU。Marc Zyngier 对补丁进行了审核并表示认可。整体来看，这些补丁旨在提升 KVM 对 PMU 寄存器的支持，确保在不同环境下的稳定性和一致性。

#### 📝 邮件列表

1. **[03-15 18:12]** [PATCH v5 0/5] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
2. **[03-15 18:12]** [PATCH v5 1/5] KVM: arm64: PMU: Set raw values from user to
 PM{C,I}NTEN{SET,CLR}, PMOVS{SET,CLR}
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
3. **[03-15 18:12]** [PATCH v5 2/5] KVM: arm64: PMU: Assume PMU presence in pmu-emul.c
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
4. **[03-15 18:12]** [PATCH v5 3/5] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
5. **[03-15 18:12]** [PATCH v5 4/5] KVM: arm64: PMU: Reload when user modifies
 registers
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
6. **[03-15 18:12]** [PATCH v5 5/5] KVM: arm64: PMU: Reload when resetting
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
7. **[03-16 10:33]** Re: [PATCH v5 0/5] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH v3 0/1] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 10 Mar 2025 10:30:07 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（内核虚拟机）的补丁，旨在允许在 arm64 架构上将 GPU 设备内存映射为可缓存。补丁的主要内容是解决当前 KVM 强制将内存区域标记为 NORMAL 或 DEVICE_nGnRE 的限制，使得未添加到内核的设备内存也能被标记为可缓存。

在历史讨论中，参与者们针对补丁的 v2 版本提出了多项建议，最终形成了 v3 版本。补丁通过检查 VMA（虚拟内存区域）标志中的 VM_PFNMAP 来判断内存的缓存性，如果 pgprot 映射类型为 MT_NORMAL，则认为该内存可以安全地映射为可缓存。

本周的讨论中，Ankit Agrawal 提出了补丁的更新，并对之前的建议进行了响应。Marc Zyngier 提出了关于错误处理和用户空间如何了解支持的功能的担忧，强调在 memslot 注册时应进行检查，以避免用户空间在不支持的情况下进行映射。Ankit 同意这一观点，并表示将添加相应的检查。

最终，讨论集中在如何有效地向用户空间传达 KVM 的新行为，以及如何在用户空间进行 mmap 操作时处理 FWB（Fault Write Buffer）的问题。参与者一致认为，应该在 memslot 创建时进行检查，并返回错误，以确保用户空间能够理解当前的支持情况。

#### 📝 邮件列表

1. **[03-10 10:30]** [PATCH v3 0/1] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[03-10 10:30]** [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
3. **[03-10 11:54]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-11 03:42]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
5. **[03-11 11:18]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-11 12:07]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
7. **[03-12 08:21]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH v4 0/3] Count pKVM stage-2 usage in secondary pagetable stat

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 13 Mar 2025 11:40:35 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁系列（PATCH v4 0/3），旨在统计 pKVM 在二级页表中的使用情况。该补丁系列的主要内容是允许在使用 pKVM 时计算与二级页表相关的内存，并在 `/proc/meminfo` 的 `SecPageTables` 字段中显示该值。

在历史讨论中，补丁经历了多次修改，主要集中在以下几个方面：增加了对 `kvm_hyp_memcache` 的标志支持，以便根据内存缓存配置进行内存统计；为二级页表的内存回收引入了独立的内存缓存；并确保在统计中考虑 PGD（页全局目录）。

本周的新讨论中，Vincent Donnefort 提交了三个补丁，分别是：
1. 为 `kvm_hyp_memcache` 添加标志。
2. 为二级页表的 pKVM 拆解引入独立的内存缓存。
3. 统计 pKVM 在二级页表中的使用情况。

这些补丁得到了参与者的认可，Marc Zyngier 表示支持并确认了补丁，Oliver Upton 则表示已将其应用到下一个版本中。整体来看，本周的讨论进展顺利，补丁已成功合并。

#### 📝 邮件列表

1. **[03-13 11:40]** [PATCH v4 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-13 11:40]** [PATCH v4 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-13 11:40]** [PATCH v4 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-13 11:40]** [PATCH v4 3/3] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[03-13 13:13]** Re: [PATCH v4 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-14 16:11]** Re: [PATCH v4 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 16: [PATCH v3 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Mar 2025 11:18:28 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM（Kernel-based Virtual Machine）在 arm64 架构下初始化 HCRX_EL2 和其他陷阱的问题。Fuad Tabba 提出了一个包含四个补丁的补丁集（PATCH v3 0/4），旨在改善 pKVM 的实现。

在历史讨论中，补丁的主要目标是将设置 HCRX_EL2 陷阱的代码重构为独立函数，并在 pKVM 中初始化这些陷阱。补丁集的结构包括：1）将设置 HCRX_EL2 陷阱的逻辑提取到单独的函数中；2）在 pKVM 中初始化 HCRX_EL2 陷阱；3）将 pKVM hypervisor vcpu 的创建逻辑提取为独立函数；4）在对应的主机 vcpu 运行后再创建每个 pKVM hypervisor vcpu。

本周的讨论中，Fuad 提供了补丁的更新，移除了 WRITE_ONCE 的使用，并将补丁基于 Linux 6.14-rc6 进行了重整。所有补丁均得到了 Marc Zyngier 和 Will Deacon 的审核与认可。最终，Oliver Upton 确认了这些补丁将被应用到下一个版本中，标志着讨论的成功结束。

#### 📝 邮件列表

1. **[03-14 11:18]** [PATCH v3 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[03-14 11:18]** [PATCH v3 1/4] KVM: arm64: Factor out setting HCRX_EL2 traps into
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[03-14 11:18]** [PATCH v3 2/4] KVM: arm64: Initialize HCRX_EL2 traps in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[03-14 11:18]** [PATCH v3 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[03-14 11:18]** [PATCH v3 4/4] KVM: arm64: Create each pKVM hyp vcpu after its
 corresponding host vcpu
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[03-14 16:11]** Re: [PATCH v3 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps in pKVM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 17: [PATCH] KVM: arm64: Drop sort_memblock_regions()

**📧 邮件数**: 5 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 11 Mar 2025 14:37:18 +1000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中的一个补丁，旨在删除 `sort_memblock_regions()` 函数。Gavin Shan 提出的补丁指出，内存区域在通过 `memblock_add()` 添加时已经正确排序，因此不需要再进行额外的排序。该补丁实际上是对之前提交的 commit a14307f5310c 的回退，意在简化代码，且不引入功能上的变化。

在之前的讨论中，Gavin 通过代码检查发现了不必要的排序操作，并希望确认这一点，因此将 Quentin Perret 也抄送到邮件中。Anshuman Khandual 提出了对该补丁的疑问，询问促使这一变更的原因。Gavin 解释说，最初的排序是因为早期版本中需要注册保留区域，但现有代码不再需要此操作。

本周的讨论中，Will Deacon 和 Quentin Perret 对补丁表示认可，认为在当前代码结构下，删除排序不会导致问题。Quentin 进一步确认了这一点，并表示支持该补丁。整体来看，本周的讨论主要集中在对补丁的确认和认可上，未提出新的反对意见。

#### 📝 邮件列表

1. **[03-11 14:37]** [PATCH] KVM: arm64: Drop sort_memblock_regions()
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[03-13 08:23]** Re: [PATCH] KVM: arm64: Drop sort_memblock_regions()
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[03-13 16:09]** Re: [PATCH] KVM: arm64: Drop sort_memblock_regions()
   - 发件人: Gavin Shan <gshan@redhat.com>
4. **[03-13 11:26]** Re: [PATCH] KVM: arm64: Drop sort_memblock_regions()
   - 发件人: Will Deacon <will@kernel.org>
5. **[03-13 19:08]** Re: [PATCH] KVM: arm64: Drop sort_memblock_regions()
   - 发件人: Quentin Perret <qperret@google.com>

---

### Thread 18: [PATCH] KVM: arm64: Writable TGRAN*_2

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Mar 2025 19:40:13 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，标题为「[PATCH] KVM: arm64: Writable TGRAN*_2」。该补丁的目的是允许用户空间写入 ID_AA64MMFR0_EL1.TGRAN*_2 的安全值（NI），并禁止对 NV 字段进行更改，因为 KVM 提供了基于 PAGE_SIZE 的安全视图。此外，补丁还包括对 set_id_regs 自测的更新。

在历史讨论中，Sebastian Ott 提出了这个补丁，并提供了相关的代码更改。讨论的重点在于补丁的基础提交未明确说明，导致与当前的 6.14 rc 版本不兼容。

在本周的新讨论中，Oliver Upton 指出补丁与先前的提交存在冲突，并表示将会处理这些问题并将补丁排入队列。Sebastian 也确认了补丁的基础版本，并表示感谢。最终，Oliver 确认补丁已被应用到下一个版本中。

总结而言，本周的讨论主要集中在补丁的兼容性和冲突解决上，最终达成了将补丁应用于下一个版本的共识。

#### 📝 邮件列表

1. **[03-06 19:40]** [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[03-12 10:20]** Re: [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-12 10:32]** Re: [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[03-12 18:33]** Re: [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Sebastian Ott <sebott@redhat.com>
5. **[03-12 14:04]** Re: [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 19: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 27 Feb 2025 09:21:19 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH V3），其目的是启用 EL2 对 FEAT_PMUv3p9 的要求。补丁的核心内容是添加一个新的初始化帮助函数 `__init_el2_fgt2()`，该函数用于配置 FEAT_FGT2 相关的细粒度陷阱控制寄存器，以确保在 EL1 中对 PMU 寄存器的访问不会引发陷阱。

在历史讨论中，Anshuman Khandual 提出了这个补丁，并详细说明了在 EL1 访问特定 PMU 寄存器时需要进行的 EL2 配置，以避免陷阱问题。该补丁的必要性在于确保系统的稳定性和功能性。

在本周的新讨论中，Catalin Marinas 确认已将该补丁应用到 arm64 的开发分支，并指出在补丁被合并到主线后，应该直接将其发送到稳定版本中，以避免因自动回溯而导致的构建问题。Anshuman Khandual 也表示会按照建议进行操作。

总体而言，本周的讨论主要集中在补丁的应用和后续处理上，确保其在主线合并后的稳定性。

#### 📝 邮件列表

1. **[02-27 09:21]** [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[03-11 17:17]** Re: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[03-12 09:16]** Re: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 20: [PATCH 07/18] KVM: arm64: Compute FGT masks from KVM's own FGT tables

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 4 Mar 2025 16:55:50 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构下的补丁，主题为“从 KVM 自身的 FGT 表计算 FGT 掩码”。该补丁旨在解决 HFGxTR 寄存器处理中的一些问题。

在历史讨论中，Marc Zyngier 提出了一个关于手工制作的位掩码 __HFGRTR_ONLY_MASK 的潜在问题，指出如果不更新该掩码，可能会导致错误的位设置，从而影响系统的正常运行。

本周的新讨论中，Marc Zyngier 进一步回应了 Fuad Tabba 的观点，承认之前提到的问题确实存在，并表示他将采取措施彻底解决 HFGxTR 的复杂性。他决定完全去除 HFGxTR 的相关代码，使 HFG{R,W}TR 寄存器的定义更加清晰。Marc 提到这次修改涉及多个文件，尽管修改量较大，但这样做可以避免对寄存器的错误假设，提升代码的可维护性。他计划在下周一重新发布这一系列补丁。

总结而言，本周的进展主要是对 HFGxTR 处理的重大改进，旨在提高 KVM 在 arm64 架构下的稳定性和可读性。

#### 📝 邮件列表

1. **[03-04 16:55]** Re: [PATCH 07/18] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[03-10 11:42]** Re: [PATCH 07/18] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-11 19:10]** Re: [PATCH 07/18] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH] KVM: arm64: Tear down vGIC on failed vCPU creation

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Mar 2025 13:34:09 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的补丁，主题为“在 vCPU 创建失败时拆除 vGIC”。该补丁的主要内容是，当 `kvm_arch_vcpu_create()` 函数在尝试与 hypervisor 共享 vCPU 页时失败时，之前未能清理 vGIC vCPU 数据，可能导致内存泄漏或使用后释放的问题。补丁通过在错误情况下添加必要的清理代码，确保 vGIC vCPU 结构被正确销毁。

在历史讨论中，虽然没有具体的补丁或问题被提及，但提到了一些相关的提交记录，表明在早期版本中，创建映射的过程可能会失败，从而导致当前问题的出现。

在本周的新讨论中，Will Deacon 提出了该补丁，并详细说明了其必要性和实现方式。Marc Zyngier 对该补丁进行了审核并表示支持，确认了补丁的有效性。这表明该补丁得到了积极的反馈，并可能在未来的版本中被合并。

#### 📝 邮件列表

1. **[03-14 13:34]** [PATCH] KVM: arm64: Tear down vGIC on failed vCPU creation
   - 发件人: Will Deacon <will@kernel.org>
2. **[03-16 10:38]** Re: [PATCH] KVM: arm64: Tear down vGIC on failed vCPU creation
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 10 Mar 2025 12:08:36 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM64 架构中内存管理的一个补丁系列，主要内容是删除 PXD_TABLE_BIT。该补丁系列包含八个部分，涉及对内存页表的不同处理和检查。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁的提出是为了简化 ARM64 的内存管理机制，特别是在处理页表时，去除不必要的标志位以提高效率。

在本周的新讨论中，参与者 Anshuman Khandual 对补丁系列进行了温和的提醒，询问是否有任何异议。随后，Catalin Marinas 确认已将该补丁应用到 ARM64 的开发分支中，表示感谢。这表明该补丁系列得到了认可，并且已经进入了实际的开发流程。

总结而言，本周的讨论确认了补丁的有效性和应用进展，标志着 ARM64 内存管理的进一步优化。

#### 📝 邮件列表

1. **[03-10 12:08]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[03-12 18:09]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 23: [PATCH V2 1/8] KVM: arm64: ptdump: Test PMD_TYPE_MASK for block
 mapping

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 11 Mar 2025 18:10:31 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“[PATCH V2 1/8] KVM: arm64: ptdump: Test PMD_TYPE_MASK for block mapping”。该补丁的目的是测试 PMD_TYPE_MASK，以确保在块映射中正确处理页表项。

在历史讨论中，并没有提供具体的背景信息，但可以推测，该补丁是为了增强 KVM 在处理内存管理方面的稳定性和准确性。

在本周的新讨论中，参与者 Catalin Marinas 向 Marc Zyngier 和 Oliver 询问是否同意将该补丁合并到 arm64 的代码树中。Marc Zyngier 随后表示他对此补丁没有异议，并给予了“Acked-by”的确认，表明他支持该补丁的合并。这表明该补丁得到了积极的反馈，并可能会在未来的版本中被采纳。整体来看，本周的讨论进展顺利，为补丁的实施铺平了道路。

#### 📝 邮件列表

1. **[03-11 18:10]** Re: [PATCH V2 1/8] KVM: arm64: ptdump: Test PMD_TYPE_MASK for block
 mapping
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[03-11 18:22]** Re: [PATCH V2 1/8] KVM: arm64: ptdump: Test PMD_TYPE_MASK for block
 mapping
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH 0/4] arm64: mitigate CVE-2024-7881 in the absence of firmware mitigation

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 14 Mar 2025 18:37:25 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 CVE-2024-7881 漏洞的补丁系列，主要针对 arm64 架构，在缺乏固件缓解措施的情况下进行缓解。

**原始 patch/问题的内容**：
本次补丁系列包含四个补丁，旨在通过修改 CPU 特性和 KVM 相关代码来缓解 CVE-2024-7881 漏洞。具体补丁包括重命名和提取 CPU 特性函数，以及在 KVM 中向虚拟机暴露特定的架构工作区。

**之前讨论要点**：
在历史讨论中，补丁的初步版本已被提出，但并未引起广泛的审查。尽管有少量参与者（如 Oliver）对 KVM 部分进行了审查，整体反馈较少。

**本周的新讨论、进展或结论**：
在本周的讨论中，参与者 Catalin Marinas 确认已将补丁应用到 arm64 的开发分支中，并表示补丁看起来没有问题。虽然审查反馈不多，但他欢迎其他人提出意见或要求删除补丁。补丁系列的进一步工作也被提及，显示出对该问题的持续关注和后续开发的可能性。

#### 📝 邮件列表

1. **[03-14 18:37]** Re: [PATCH 0/4] arm64: mitigate CVE-2024-7881 in the absence of firmware mitigation
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC kvmtool 0/9] arm: Drop support for 32-bit kvmtool

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 14 Mar 2025 15:25:07 -0700

#### 🤖 AI 总结

本邮件线程讨论了对 KVM 工具的一个重要补丁，主要内容是取消对 32 位 KVM/ARM 的支持。以下是讨论的主要要点：

1. **原始补丁内容**：补丁的核心是删除对 32 位 KVM/ARM 的支持。考虑到最后一个支持 32 位 KVM 的稳定内核版本为 5.4，并且该版本预计将在今年年底结束支持，开发者认为此时是移除该功能的合适时机。

2. **之前的讨论要点**：在历史讨论中，开发者指出 32 位 KVM 的使用率一直很低，并且 32 位 KVM 在 64 位 KVM 中并不影响对 32 位客户机的支持。因此，移除这一功能是合理的。

3. **本周的新讨论与进展**：本周的讨论中，开发者 Oliver Upton 提出了多个补丁，逐步整合和重构 ARM 相关的代码，主要包括：
   - 移动 ARM64 特有的功能到主目录。
   - 合并 ARM 和 ARM64 的 kvm.c 文件。
   - 删除冗余的头文件，并将其移动到更合适的位置。
   - 重命名顶层目录以符合内核的命名规范。

这些补丁的实施将进一步简化代码结构，提高维护性，同时确保 64 位 KVM 仍然能够支持 32 位客户机。整体来看，讨论围绕着优化和清理代码，确保 KVM 工具的现代化与高效性。

#### 📝 邮件列表

1. **[03-14 15:25]** [RFC kvmtool 0/9] arm: Drop support for 32-bit kvmtool
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[03-14 15:25]** [RFC kvmtool 1/9] Drop support for 32-bit arm
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-14 15:25]** [RFC kvmtool 2/9] arm64: Move arm64-only features into main directory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[03-14 15:25]** [RFC kvmtool 3/9] arm64: Combine kvm.c
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[03-14 15:25]** [RFC kvmtool 4/9] arm64: Merge kvm-cpu.c
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[03-14 15:25]** [RFC kvmtool 5/9] arm64: Combine kvm-config-arch.h
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[03-14 15:25]** [RFC kvmtool 6/9] arm64: Move remaining kvm/* headers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[03-14 15:25]** [RFC kvmtool 7/9] arm64: Move asm headers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[03-14 15:25]** [RFC kvmtool 8/9] arm64: Rename top-level directory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[03-14 15:25]** [RFC kvmtool 9/9] arm64: Get rid of the 'arm-common' include directory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/5] arm64: Change the default QEMU CPU type to "max"

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 14 Mar 2025 15:49:00 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于对 KVM 单元测试的补丁系列，主要目的是将 ARM64 的默认 QEMU CPU 类型更改为 "max"。该补丁系列的版本为 v2，共包含五个补丁。

在历史讨论中，补丁的初始版本（v1）由 Alexandru 提出，主要集中在清理配置标志和设置默认 CPU 类型。反馈意见促使开发者们区分了 `--processor` 和新引入的 `--qemu-cpu` 选项，以便分别配置构建和运行时标志。

本周的新讨论中，Jean-Philippe Brucker 详细介绍了补丁的具体内容，包括：
1. 通过 `./configure` 命令设置正确的默认处理器类型，确保在 ARM 和 ARM64 架构下显示合适的默认值。
2. 引入 `--qemu-cpu` 选项，以便用户能够设置运行时的 CPU 类型，默认值为 "max"，以便启用所有最新的 TCG 特性。
3. 解决了在 ARM64 架构下，构建系统未能正确传递 `-mcpu` 参数的问题。

最终，补丁的实施将使得 KVM 单元测试能够更好地支持最新的 ARM64 特性，并提高测试的灵活性和准确性。

#### 📝 邮件列表

1. **[03-14 15:49]** [kvm-unit-tests PATCH v2 0/5] arm64: Change the default QEMU CPU type to "max"
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>
2. **[03-14 15:49]** [kvm-unit-tests PATCH v2 1/5] configure: arm64: Don't display 'aarch64' as the default architecture
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>
3. **[03-14 15:49]** [kvm-unit-tests PATCH v2 2/5] configure: arm/arm64: Display the correct default processor
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>
4. **[03-14 15:49]** [kvm-unit-tests PATCH v2 3/5] arm64: Implement the ./configure --processor option
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>
5. **[03-14 15:49]** [kvm-unit-tests PATCH v2 4/5] configure: Add --qemu-cpu option
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>
6. **[03-14 15:49]** [kvm-unit-tests PATCH v2 5/5] arm64: Use -cpu max as the default for TCG
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>

---

### Thread 2: [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  7 Mar 2025 10:18:29 +0100

#### 🤖 AI 总结

本邮件讨论主题为“[kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option”，主要涉及在使用 Clang 进行交叉编译时，如何在 Makefile 中正确处理 CFLAGS 变量的问题。

历史讨论中，Andrew Jones 提出了一个补丁，目的是在 cc-option 中引入 CFLAGS，以确保在交叉编译时能够识别目标特定的选项。他指出，缺少 CFLAGS 会导致编译失败，特别是在 x86 构建中。补丁还引入了 realmode_bits 变量，以避免 make 构建时出现循环引用的问题。

在本周的新讨论中，Thomas Huth 对该补丁进行了审核并表示支持，标记为“Reviewed-by”。Alexandru Elisei 也对补丁进行了测试，确认在使用 Clang 编译 MTE 测试时能够正常工作，并表示感谢 Andrew 的调试工作。整体来看，补丁得到了积极的反馈，且已通过测试，表明修复有效。

#### 📝 邮件列表

1. **[03-07 10:18]** [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[03-13 08:50]** Re: [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option
   - 发件人: Thomas Huth <thuth@redhat.com>
3. **[03-13 10:11]** Re: [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

