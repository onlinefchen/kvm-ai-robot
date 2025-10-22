# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 08:27:36

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 220
- **总 Thread 数**: 28
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 21 threads (192 邮件)
- **RFC**: 1 threads (3 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Other**: 5 threads (23 邮件)

---

## 📌 PATCH

共 21 个 thread

---

### Thread 1: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events

**📧 邮件数**: 36 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 3 Mar 2025 09:36:20 +1000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）的补丁系列，特别是第一个补丁“[PATCH v7 01/45] KVM: Prepare for handling only shared mappings in mmu_notifier events”。该补丁旨在为处理仅共享映射的 mmu_notifier 事件做准备。

在历史讨论中，Gavin Shan 指出补丁中新增的成员（only_private 和 only_shared）与 attr_filter 的成员重复，后者可以设置为 KVM_FILTER_SHARED、KVM_FILTER_PRIVATE 或两者兼有。他提到这个问题是在 dca6c88532322 提交之后才显现出来的。

在本周的新讨论中，参与者们对多个补丁进行了审查和反馈。Gavin Shan 对 Steven Price 提出的补丁进行了逐一审查，提出了一些代码改进建议，并标记为“Reviewed-by”。讨论中还涉及了对补丁描述的澄清，特别是关于调试能力的暴露，Steven 指出当前的补丁并不引入新功能，而是隐藏了不支持的调试能力。此外，Gavin 和 Steven 还讨论了如何更好地区分页面和粒度（granule），以支持未来的 ARM CCA（控制器访问）功能。

总体而言，本周的讨论集中在对补丁的细节审查、代码改进建议以及对补丁描述的澄清上，显示出参与者们对优化 KVM 代码的持续关注和努力。

#### 📝 邮件列表

1. **[03-03 09:36]** Re: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[03-03 13:42]** Re: [PATCH v7 05/45] arm64: RME: Add wrappers for RMI calls
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[03-03 13:58]** Re: [PATCH v7 06/45] arm64: RME: Check for RME support at KVM init
   - 发件人: Gavin Shan <gshan@redhat.com>
4. **[03-03 14:10]** Re: [PATCH v7 07/45] arm64: RME: Define the user ABI
   - 发件人: Gavin Shan <gshan@redhat.com>
5. **[03-03 14:42]** Re: [PATCH v7 08/45] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Gavin Shan <gshan@redhat.com>
6. **[03-03 14:48]** Re: [PATCH v7 09/45] kvm: arm64: Expose debug HW register numbers for
 Realm
   - 发件人: Gavin Shan <gshan@redhat.com>
7. **[03-03 14:53]** Re: [PATCH v7 10/45] arm64: kvm: Allow passing machine type in KVM
 creation
   - 发件人: Gavin Shan <gshan@redhat.com>
8. **[03-03 16:25]** Re: [PATCH v7 11/45] arm64: RME: RTT tear down
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[03-03 17:08]** Re: [PATCH v7 12/45] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Gavin Shan <gshan@redhat.com>
10. **[03-03 15:05]** Re: [PATCH v7 01/45] KVM: Prepare for handling only shared mappings
 in mmu_notifier events
   - 发件人: Steven Price <steven.price@arm.com>
11. **[03-03 15:05]** Re: [PATCH v7 05/45] arm64: RME: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
12. **[03-03 18:02]** Re: [PATCH v7 14/45] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[03-04 10:45]** Re: [PATCH v7 16/45] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
14. **[03-04 11:03]** Re: [PATCH v7 17/45] arm64: RME: Handle realm enter/exit
   - 发件人: Gavin Shan <gshan@redhat.com>
15. **[03-04 14:35]** Re: [PATCH v7 18/45] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Gavin Shan <gshan@redhat.com>
16. **[03-04 14:52]** Re: [PATCH v7 19/45] KVM: arm64: Handle realm MMIO emulation
   - 发件人: Gavin Shan <gshan@redhat.com>
17. **[03-04 15:09]** Re: [PATCH v7 20/45] arm64: RME: Allow populating initial contents
   - 发件人: Gavin Shan <gshan@redhat.com>
18. **[03-04 15:15]** Re: [PATCH v7 22/45] KVM: arm64: Handle realm VCPU load
   - 发件人: Gavin Shan <gshan@redhat.com>
19. **[03-04 15:29]** Re: [PATCH v7 23/45] KVM: arm64: Validate register access for a Realm
 VM
   - 发件人: Gavin Shan <gshan@redhat.com>
20. **[03-04 15:38]** Re: [PATCH v7 24/45] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Gavin Shan <gshan@redhat.com>
21. **[03-04 15:39]** Re: [PATCH v7 25/45] KVM: arm64: WARN on injected undef exceptions
   - 发件人: Gavin Shan <gshan@redhat.com>
22. **[03-04 15:42]** Re: [PATCH v7 26/45] arm64: Don't expose stolen time for realm guests
   - 发件人: Gavin Shan <gshan@redhat.com>
23. **[03-04 15:47]** Re: [PATCH v7 27/45] arm64: rme: allow userspace to inject aborts
   - 发件人: Gavin Shan <gshan@redhat.com>
24. **[03-04 16:01]** Re: [PATCH v7 28/45] arm64: rme: support RSI_HOST_CALL
   - 发件人: Gavin Shan <gshan@redhat.com>
25. **[03-04 16:02]** Re: [PATCH v7 29/45] arm64: rme: Allow checking SVE on VM instance
   - 发件人: Gavin Shan <gshan@redhat.com>
26. **[03-04 16:23]** Re: [PATCH v7 30/45] arm64: RME: Always use 4k pages for realms
   - 发件人: Gavin Shan <gshan@redhat.com>
27. **[03-04 16:27]** Re: [PATCH v7 31/45] arm64: rme: Prevent Device mappings for Realms
   - 发件人: Gavin Shan <gshan@redhat.com>
28. **[03-04 21:51]** Re: [PATCH v7 34/45] kvm: rme: Hide KVM_CAP_READONLY_MEM for realm
 guests
   - 发件人: Gavin Shan <gshan@redhat.com>
29. **[03-04 17:59]** Re: [PATCH v7 15/45] KVM: arm64: Support timers in realm RECs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
30. **[03-05 09:45]** Re: [PATCH v7 35/45] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
31. **[03-05 09:46]** Re: [PATCH v7 36/45] arm64: RME: Set breakpoint parameters through
 SET_ONE_REG
   - 发件人: Gavin Shan <gshan@redhat.com>
32. **[03-05 10:15]** Re: [PATCH v7 05/45] arm64: RME: Add wrappers for RMI calls
   - 发件人: Gavin Shan <gshan@redhat.com>
33. **[03-05 13:53]** Re: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>
34. **[03-05 16:25]** Re: [PATCH v7 09/45] kvm: arm64: Expose debug HW register numbers for
 Realm
   - 发件人: Steven Price <steven.price@arm.com>
35. **[03-06 09:31]** Re: [PATCH v7 09/45] kvm: arm64: Expose debug HW register numbers for
 Realm
   - 发件人: Gavin Shan <gshan@redhat.com>
36. **[03-07 15:43]** Re: [PATCH v7 12/45] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 2: [PATCH v2 0/4] KVM: arm64: Fix initializing HCRX_EL2 and other traps
 in pKVM

**📧 邮件数**: 31 | **👥 参与者**: 6 | **📅 开始时间**: Wed, 26 Feb 2025 21:55:16 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁，主要集中在 HCRX_EL2 的初始化及其他陷阱的处理。

1. **原始补丁内容**：Fuad Tabba 提出的补丁系列（PATCH v2 0/4）旨在修复 pKVM 中 HCRX_EL2 的初始化问题，主要通过将 HCRX_EL2 陷阱的设置分离到一个独立的函数中，从而在受保护和非受保护模式之间共享逻辑。此外，还重构了 pKVM 的虚拟 CPU 创建过程。

2. **之前讨论要点**：历史讨论中，参与者们关注补丁的兼容性与稳定性，特别是与 Android 代码的一致性问题。关于如何处理 WRITE_ONCE 和 READ_ONCE 的使用，以及是否需要在 MMU 通知中重新考虑锁的保护等问题，讨论较为深入。

3. **本周新讨论与进展**：本周的讨论主要围绕补丁的具体实现细节展开。Will Deacon 提出了一些关于并发性和潜在竞争条件的疑问，特别是涉及到 MMU 通知和虚拟 CPU 状态的初始化。Sebastian Ene 也对 FF-A 缓冲区的映射进行了讨论，提出可能需要对补丁进行修改以避免不必要的复杂性。此外，关于补丁是否适合在即将发布的 v6.15 中合并，参与者们达成了一致，认为在经过审查后可以将其纳入。

总体来看，邮件讨论围绕补丁的实现细节、潜在问题及其对未来版本的影响展开，参与者们积极交流以确保补丁的质量和稳定性。

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
4. **[02-27 18:17]** [PATCH v2 1/4] KVM: arm64: Use the static initializer for the vesion lock
   - 发件人: Sebastian Ene <sebastianene@google.com>
5. **[02-27 18:17]** [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the
 ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
6. **[02-27 18:17]** [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
7. **[02-27 18:17]** [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx buffer
 to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
8. **[02-27 20:25]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
9. **[02-27 23:12]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
10. **[02-28 10:09]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to the ffa header
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-28 19:44]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Quentin Perret <qperret@google.com>
12. **[03-03 07:57]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[03-03 19:18]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>
14. **[03-03 19:21]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[03-03 21:49]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Will Deacon <will@kernel.org>
16. **[03-03 23:43]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
17. **[03-03 23:44]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Will Deacon <will@kernel.org>
18. **[03-04 00:38]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sebastian Ene <sebastianene@google.com>
19. **[03-04 00:53]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
20. **[03-04 01:56]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
21. **[03-04 09:54]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
22. **[03-04 09:57]** Re: [PATCH v2 2/4] KVM: arm64: Move the ffa_to_linux definition to
 the ffa header
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
23. **[03-04 12:33]** Re: [PATCH v2 3/4] KVM: arm64: Factor out pKVM hyp vcpu creation to
 separate function
   - 发件人: Fuad Tabba <tabba@google.com>
24. **[03-04 17:38]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
25. **[03-05 00:38]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Will Deacon <will@kernel.org>
26. **[03-05 00:39]** Re: [PATCH v2 1/4] KVM: arm64: Use the static initializer for the
 vesion lock
   - 发件人: Will Deacon <will@kernel.org>
27. **[03-05 00:45]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Will Deacon <will@kernel.org>
28. **[03-05 09:41]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
29. **[03-05 18:36]** Re: [PATCH v2 3/4] KVM: arm64: Map the hypervisor FF-A buffers on
 ffa init
   - 发件人: Sebastian Ene <sebastianene@google.com>
30. **[03-05 19:34]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Will Deacon <will@kernel.org>
31. **[03-06 09:40]** Re: [PATCH v2 4/4] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>

---

### Thread 3: [PATCH hyperv-next v5 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 15 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Mar 2025 14:02:52 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构下支持虚拟信任级别（VTL）启动的补丁集，主要由 Roman Kisel 提出。该补丁集的目的是使 Hyper-V 代码能够在 ARM64 环境中以 VTL 模式启动，这对于实现虚拟安全模式至关重要。

在历史讨论中，补丁集经历了多个版本的迭代，主要集中在如何通过 SMCCC（标准化的多处理器调用约定）检测 Hyper-V 的存在，并优化了代码结构与功能。补丁集的关键改进包括引入了一个通用的 API 来检测 Hyper-V，修复了与 ACPI 相关的依赖问题，并确保在非 ACPI 系统上也能正常工作。

在本周的新讨论中，Roman Kisel 提交了多个补丁，涵盖了 VTL 模式的启用、VTL 字段的初始化、以及如何从设备树中获取中断配置等。Arnd Bergmann 对部分补丁给予了认可，并提出了一些优化建议，如调整 Kconfig 依赖关系的顺序，以提高逻辑清晰度。

总的来说，本周的讨论集中在补丁的细节实现和代码优化上，推动了 ARM64 下 Hyper-V 的 VTL 支持进展。

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
14. **[03-08 22:08]** Re: [PATCH hyperv-next v5 01/11] arm64: kvm, smccc: Introduce and use API for
 detectting hypervisor presence
   - 发件人: Arnd Bergmann <arnd@arndb.de>
15. **[03-08 22:11]** Re: [PATCH hyperv-next v5 08/11] Drivers: hv: vmbus: Get the IRQ number from
 DeviceTree
   - 发件人: Arnd Bergmann <arnd@arndb.de>

---

### Thread 4: [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware

**📧 邮件数**: 15 | **👥 参与者**: 1 | **📅 开始时间**: Wed,  5 Mar 2025 12:26:27 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 Apple 硬件的 KVM arm64 PMUv3 特性支持的补丁集（PATCH v3 00/14）。该补丁旨在实现对 Apple M 系列处理器的性能监控单元（PMU）虚拟化支持。

补丁的主要内容包括：
1. **补丁功能**：补丁集的目标是支持 Apple 硬件上的 PMUv3 特性，使 KVM 能够虚拟化 PMU 事件。补丁包括对事件选择和过滤配置的重构、PMU 事件的映射、合成系统寄存器的计算等。

2. **历史讨论要点**：虽然本周没有提及具体的历史讨论，但补丁的版本更新（从 v2 到 v3）表明开发者在回应之前的反馈，进行了结构调整和细节修正。

3. **本周新讨论与进展**：本周的讨论集中在补丁的具体实现上，包括：
   - 重新组织补丁以包含 PMUv3 事件的映射。
   - 支持主机和客户机的事件过滤。
   - 计算 PMCEID 值以支持虚拟化。
   - 确保对 SW_INCR 事件的无条件支持。
   - 通过 cpucap 检测系统是否支持 PMUv3。
   - 在 Apple M 处理器上启用 IMPDEF PMUv3 陷阱。

整体来看，该补丁集的实施将增强 KVM 在 Apple 硬件上的性能监控能力，为虚拟化提供更强的支持。

#### 📝 邮件列表

1. **[03-05 12:26]** [PATCH v3 00/14] KVM: arm64: FEAT_PMUv3 on Apple hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[03-05 12:26]** [PATCH v3 01/14] drivers/perf: apple_m1: Refactor event select/filter configuration
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-05 12:26]** [PATCH v3 02/14] drivers/perf: apple_m1: Support host/guest event filtering
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[03-05 12:26]** [PATCH v3 03/14] KVM: arm64: Compute PMCEID from arm_pmu's event bitmaps
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[03-05 12:26]** [PATCH v3 04/14] KVM: arm64: Always support SW_INCR PMU event
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[03-05 12:26]** [PATCH v3 05/14] KVM: arm64: Use a cpucap to determine if system supports FEAT_PMUv3
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[03-05 12:26]** [PATCH v3 06/14] KVM: arm64: Drop kvm_arm_pmu_available static key
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[03-05 12:26]** [PATCH v3 07/14] KVM: arm64: Use guard() to cleanup usage of arm_pmus_lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[03-05 12:26]** [PATCH v3 08/14] KVM: arm64: Move PMUVer filtering into KVM code
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[03-05 12:26]** [PATCH v3 09/14] KVM: arm64: Compute synthetic sysreg ESR for Apple PMUv3 traps
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[03-05 12:26]** [PATCH v3 10/14] KVM: arm64: Advertise PMUv3 if IMPDEF traps are present
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[03-05 12:26]** [PATCH v3 11/14] KVM: arm64: Remap PMUv3 events onto hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[03-05 12:26]** [PATCH v3 12/14] drivers/perf: apple_m1: Provide helper for mapping PMUv3 events
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[03-05 12:30]** [PATCH v3 13/14] KVM: arm64: Provide 1 event counter on IMPDEF hardware
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[03-05 12:30]** [PATCH v3 14/14] arm64: Enable IMP DEF PMUv3 traps on Apple M*
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 5: [PATCH v2 00/14] arm: rework id register storage

**📧 邮件数**: 15 | **👥 参与者**: 1 | **📅 开始时间**: Wed,  5 Mar 2025 17:38:05 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是对 ARM 架构的 ID 寄存器存储进行重构，主要通过一系列补丁（PATCH v2 00/14 至 14/14）来实现。

1. **原始补丁/问题内容**：
   该补丁系列旨在改善 ARM 架构中 ID 寄存器的存储方式，主要通过将寄存器定义从结构体字段转移到数组中，以便于管理和访问。

2. **之前讨论要点**：
   在之前的讨论中，参与者提到需要将 ID 寄存器的定义从 Linux 的 sysregs 文件中生成，并且希望在补丁中加入对 KVM 可写 ID 寄存器的支持。补丁中还包括了对宏的增强和对重复定义的修复。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在补丁的逐步提交上，Eric Auger 提交了多个补丁，逐步实现了对 ID 寄存器的存储、生成和访问的重构。补丁中引入了新的脚本，用于从 Linux 源代码生成系统寄存器定义，确保补丁与当前内核的 sysregs 结构相匹配。此外，补丁还包含了对 ID 寄存器的访问方法的更新，确保代码的整洁和可维护性。最终，补丁系列的目标是提升 ARM CPU 模型的支持和功能。

#### 📝 邮件列表

1. **[03-05 17:38]** [PATCH v2 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[03-05 17:38]** [PATCH v2 01/14] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[03-05 17:38]** [PATCH v2 02/14] arm/kvm: add accessors for storing host features into idregs
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[03-05 17:38]** [PATCH v2 03/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[03-05 17:38]** [PATCH v2 04/14] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[03-05 17:38]** [PATCH v2 05/14] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[03-05 17:38]** [PATCH v2 06/14] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[03-05 17:38]** [PATCH v2 07/14] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[03-05 17:38]** [PATCH v2 08/14] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[03-05 17:38]** [PATCH v2 09/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[03-05 17:38]** [PATCH v2 10/14] arm/cpu: Store id_pfr0/1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[03-05 17:38]** [PATCH v2 11/14] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[03-05 17:38]** [PATCH v2 12/14] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[03-05 17:38]** [PATCH v2 13/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[03-05 17:38]** [PATCH v2 14/14] arm/cpu: Add generated files
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 6: [PATCH v2 0/3] Count pKVM stage-2 usage in secondary pagetable stat

**📧 邮件数**: 13 | **👥 参与者**: 4 | **📅 开始时间**: Tue,  4 Mar 2025 13:43:43 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 pKVM 的补丁系列，主要目的是在使用 pKVM 时统计与 stage-2 相关的内存使用情况，以便在 `/proc/meminfo` 的 `SecPageTables` 字段中显示。

**补丁内容**：
补丁系列包括三个主要部分：
1. **添加标志到 kvm_hyp_memcache**：为内存缓存添加标志，以便根据缓存配置进行内存统计。
2. **为 stage-2 使用独立的内存缓存**：在虚拟机拆除时，为 stage-2 页表使用一个独立的内存缓存，以便更好地管理内存。
3. **统计 pKVM stage-2 使用情况**：在二级页表统计中计入 pKVM 使用的页数，类似于 VHE 模式的处理。

**历史讨论要点**：
在之前的讨论中，参与者对补丁的设计和实现进行了评审，提出了改进建议，如使用指针传递内存缓存等。

**本周新讨论与进展**：
本周的讨论主要集中在补丁的具体实现细节上，Vincent Donnefort 提出了补丁的更新版本，并对参与者的反馈做出了回应。Oliver Upton 和 Marc Zyngier 也对补丁的设计提出了建议和质疑，确保补丁的逻辑清晰且符合内核的整体架构。整体上，讨论氛围积极，参与者对补丁的进一步完善表示支持。

#### 📝 邮件列表

1. **[03-04 13:43]** [PATCH v2 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-04 13:43]** [PATCH v2 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-04 13:43]** [PATCH v2 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-04 13:43]** [PATCH v2 3/3] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[03-06 23:20]** Re: [PATCH v2 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[03-07 19:55]** [PATCH v2 0/3] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
7. **[03-07 19:55]** [PATCH v2 1/3] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
8. **[03-07 19:55]** [PATCH v2 2/3] KVM: arm64: PMU: Reload when user modifies
 registers
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
9. **[03-07 19:55]** [PATCH v2 3/3] KVM: arm64: PMU: Set raw values from user to
 PM{C,I}NTEN{SET,CLR}, PMOVS{SET,CLR}
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
10. **[03-07 11:35]** Re: [PATCH v2 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[03-09 18:40]** Re: [PATCH v2 1/3] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[03-09 18:50]** Re: [PATCH v2 2/3] KVM: arm64: PMU: Reload when user modifies registers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[03-09 19:01]** Re: [PATCH v2 3/3] KVM: arm64: PMU: Set raw values from user to PM{C,I}NTEN{SET,CLR}, PMOVS{SET,CLR}
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 7: [PATCH v2 0/9] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  6 Mar 2025 11:00:29 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于为 pKVM 的非特权虚拟机（np-guests）添加支持二级大页映射（PMD_SIZE）的补丁系列。该补丁旨在优化内存映射，允许在 Stage-1 被 Hugetlbfs 或透明大页（THPs）支持时，安装 PMD 级别的映射。

在历史讨论中，补丁系列的目标是改进 pKVM 的内存管理，特别是在处理大页映射时的性能。参与者讨论了如何在现有的 KVM 架构中实现这一功能，并提出了相关的代码修改建议。

本周的新讨论中，Vincent Donnefort 提出了多个补丁，主要包括：
1. **处理 np-guest 的大页映射**：修改了相关函数以支持大于 PAGE_SIZE 的大小。
2. **添加 nr_pages 参数**：在多个 hypercall 中引入 nr_pages 参数，以支持 PMD_SIZE 的映射。
3. **优化共享和取消共享的逻辑**：通过引入新的函数和数据结构，提升了对大页映射的管理效率。
4. **引入共享 PMD_SIZE fixmap**：为了减少在处理大页时的延迟，提出了共享 PMD_SIZE fixmap 的实现。

这些补丁的实施预计将显著提高 pKVM 的性能，特别是在处理大页映射时，降低了延迟并优化了内存访问效率。讨论中还提到了一些代码的具体修改和优化建议，显示出参与者对实现细节的关注。

#### 📝 邮件列表

1. **[03-06 11:00]** [PATCH v2 0/9] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-06 11:00]** [PATCH v2 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-06 11:00]** [PATCH v2 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-06 11:00]** [PATCH v2 3/9] KVM: arm64: Add a range to __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[03-06 11:00]** [PATCH v2 4/9] KVM: arm64: Add a range to __pkvm_host_wrprotect_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[03-06 11:00]** [PATCH v2 5/9] KVM: arm64: Add a range to __pkvm_host_test_clear_young_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[03-06 11:00]** [PATCH v2 6/9] KVM: arm64: Convert pkvm_mappings to interval tree
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[03-06 11:00]** [PATCH v2 7/9] KVM: arm64: Add a range to pkvm_mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[03-06 11:00]** [PATCH v2 8/9] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[03-06 11:00]** [PATCH v2 9/9] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 8: [PATCH v4] arm64: Add basic MTE test

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 27 Feb 2025 15:22:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的基本 MTE（Memory Tagging Extension）测试的补丁（PATCH v4）。该补丁由 Vladimir Murzin 提交，旨在测试不同 MTE 模式下的标签存储访问和标签不匹配。补丁涉及多个文件的修改，总共增加了 361 行代码。

在历史讨论中，补丁的初步版本得到了参与者的关注，但并未详细展开讨论。

本周的新讨论中，Alexandru Elisei 对补丁表示认可，并给予了“Reviewed-by”标记。Andrew Jones 提出补丁在使用 Clang 编译时出现了构建失败的问题，主要是由于汇编代码中的寄存器约束与变量类型不匹配。随后，Alexandru 提出了修改建议，调整了汇编代码以解决编译问题，并指出在配置时需要正确处理 CFLAGS。最终，Andrew Jones 表示已修复了内联汇编约束的问题，并将修改应用到 arm/queue 分支中。

总结来看，该补丁经过初步审查和讨论，虽然在编译过程中遇到了一些问题，但通过参与者的协作，问题得到了有效解决，并已提交更新。

#### 📝 邮件列表

1. **[02-27 15:22]** [PATCH v4] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>
2. **[03-06 14:11]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[03-06 14:25]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>
4. **[03-06 16:31]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
5. **[03-06 16:45]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
6. **[03-06 17:11]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[03-07 09:24]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
8. **[03-07 10:26]** Re: [PATCH v4] arm64: Add basic MTE test
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 9: [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  5 Mar 2025 15:08:22 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的可写 ID 寄存器在保护模式中的处理问题，主要通过三个补丁进行修复。

1. **原始补丁内容**：补丁旨在解决在保护模式下 ID 寄存器处理中的几个问题，包括：
   - 当用户空间更改了来宾值时，CTR_EL0 在 FEAT_EVT 系统上未被捕获。
   - 如果用户空间启用了可写的“实现 ID”寄存器，VPIDR_EL2 会被设置为 0。
   - 修正能力文档中的相关描述。

2. **之前讨论要点**：在历史讨论中，未提供具体的背景信息，但可以推测出这些问题可能影响了虚拟机的稳定性和性能，尤其是在用户空间与内核空间的交互中。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现上，Oliver Upton 提出了三个补丁：
   - 第一个补丁将来宾的 CTR_EL0 值传递到 hyp VM，并调整 TID2/TID4 配置。
   - 第二个补丁在启用可写寄存器的情况下，将 MIDR_EL1 的值复制到 hyp VM。
   - 第三个补丁修正了 KVM_CAP_ARM_WRITABLE_IMP_ID_REGS 的文档，指出如果 vCPU 已创建则会返回 EINVAL 错误。

参与者 Marc Zyngier 对前两个补丁表示认可，并建议将其合并到初始化功能的函数中。最终，Oliver Upton 确认这些补丁已被应用到下一个版本中。整体来看，本周的讨论有效推动了补丁的完善与实施。

#### 📝 邮件列表

1. **[03-05 15:08]** [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[03-05 15:08]** [PATCH 1/3] KVM: arm64: Copy guest CTR_EL0 into hyp VM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-05 15:08]** [PATCH 2/3] KVM: arm64: Copy MIDR_EL1 into hyp VM when it is writable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[03-05 15:08]** [PATCH 3/3] KVM: arm64: Fix documentation for KVM_CAP_ARM_WRITABLE_IMP_ID_REGS
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[03-06 00:25]** Re: [PATCH 1/3] KVM: arm64: Copy guest CTR_EL0 into hyp VM
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-06 00:26]** Re: [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[03-05 17:01]** Re: [PATCH 0/3] KVM: arm64: Fixes for 'writable' ID registers in protected mode
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[03-06 11:52]** Re: [PATCH 2/3] KVM: arm64: Copy MIDR_EL1 into hyp VM when it is
 writable
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 10: [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 10:25:16 +0000

#### 🤖 AI 总结

本邮件线程讨论了为 pKVM 非特权虚拟机（np-guests）添加阶段二大页映射的补丁系列（共9个补丁）。补丁的主要目的是在阶段二中安装 PMD 级别的映射，特别是在阶段一由 Hugetlbfs 或 THPs 支持的情况下。

在历史讨论中，Vincent Donnefort 提出了补丁的基本架构，强调了需要处理大页映射的必要性，并提出了相应的代码修改建议。Quentin Perret 对补丁中的某些实现细节提出了担忧，特别是关于地址对齐的问题，指出当前的 fixmap 处理不支持未对齐的地址。

在本周的新讨论中，Vincent Donnefort 和 Quentin Perret 继续探讨了补丁的细节。Quentin 对于补丁中存在的双重检查表示遗憾，并考虑不再使用某些检查函数。Vincent 进一步指出 fixmap 不支持未对齐的地址，并建议在处理未对齐大小时可能只需添加警告。

总体来看，本周讨论集中在补丁的细节优化和潜在问题的解决上，参与者们对补丁的有效性和安全性进行了深入的探讨。

#### 📝 邮件列表

1. **[02-28 10:25]** [PATCH 0/9] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-28 10:25]** [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-28 10:25]** [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-28 18:54]** Re: [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Quentin Perret <qperret@google.com>
5. **[02-28 19:06]** Re: [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>
6. **[03-03 09:03]** Re: [PATCH 2/9] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[03-03 09:08]** Re: [PATCH 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 11: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 5 | **👥 参与者**: 5 | **📅 开始时间**: Tue, 18 Feb 2025 14:39:55 -0600

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构上启用分支栈采样的补丁系列（PATCH v20 00/11）。该补丁系列主要通过一种名为分支记录缓冲扩展（BRBE）的架构特性来实现，旨在提升性能监控功能。

在历史讨论中，Rob Herring 提到该补丁系列是从 Anshuman 那里接手的，并经过了 Mark 和他自己的多次重构，特别是补丁 11 的更改较多。补丁 1-7 主要是一些清理和准备工作，已在之前的邮件中发布。

在本周的新讨论中，Rob Herring 指出补丁 11 的讨论较长，可能导致参与者对后续版本的期待。Catalin Marinas 也提到 Will Deacon 可能在等待 Mark Rutland 对整个系列的审查。Mark Rutland 对补丁的整体结构表示满意，但对过滤逻辑提出了担忧，认为其复杂性较高，并不确定是否能始终适当地过滤事件。他表示会尽快处理这个问题，整体上对补丁系列持积极态度。

总结来看，该补丁系列在历史讨论中得到了清理和重构的支持，而本周的讨论则集中在对补丁的审查和潜在问题的关注上。

#### 📝 邮件列表

1. **[02-18 14:39]** [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[03-01 07:05]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Will Deacon <will@kernel.org>
3. **[03-03 10:44]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring <robh@kernel.org>
4. **[03-04 11:25]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[03-04 16:25]** Re: [PATCH v20 00/11] arm64/perf: Enable branch stack sampling
   - 发件人: Mark Rutland <mark.rutland@arm.com>

---

### Thread 12: [PATCH v3 0/3] Count pKVM stage-2 usage in secondary pagetable stat

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  7 Mar 2025 11:34:08 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 pKVM 中统计 stage-2 使用情况的补丁（PATCH v3 0/3）。该补丁系列的主要目的是在使用 pKVM 时，能够统计与 stage-2 相关的内存使用情况，并将该值记录在 `/proc/meminfo` 的 SecPageTables 字段中。

在之前的讨论中，补丁经历了多个版本的修改。主要的改动包括：在 kvm_hyp_memcache 结构中添加标志位，以便在内存分配和释放时进行更好的管理；为 stage-2 使用单独的内存缓存；并且在统计中考虑 PGD（页全局目录）。

本周的新讨论中，Vincent Donnefort 提出了三个具体的补丁：
1. **补丁 1**：为 kvm_hyp_memcache 添加标志位，并在内存分配和释放回调中传播这些标志。
2. **补丁 2**：为 stage-2 页表的拆解使用单独的内存缓存，以便更好地统计内存使用情况。
3. **补丁 3**：在内存统计中计入 pKVM 的 stage-2 使用情况，类似于 VHE 模式的处理。

这些补丁的实施将有助于更准确地管理和统计虚拟化环境中的内存使用情况，提升系统性能和资源利用率。

#### 📝 邮件列表

1. **[03-07 11:34]** [PATCH v3 0/3] Count pKVM stage-2 usage in secondary pagetable stat
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-07 11:34]** [PATCH v3 1/3] KVM: arm64: Add flags to kvm_hyp_memcache
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-07 11:34]** [PATCH v3 2/3] KVM: arm64: Distinct pKVM teardown memcache for stage-2
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[03-07 11:34]** [PATCH v3 3/3] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 13: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 4 Mar 2025 14:36:19 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM (Kernel-based Virtual Machine) 的补丁，主题为处理 arm64 架构中 FEAT_LS64* 指令的捕获。补丁的目的是改进 KVM 对特定指令的处理，以确保在虚拟化环境中正确地转发或注入异常。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的背景是为了增强 KVM 在处理 arm64 指令时的准确性和稳定性。补丁的核心是通过一个 switch 语句来简化对不同状态的处理，从而提高代码的可读性和维护性。

在本周的新讨论中，参与者 Fuad Tabba 和 Marc Zyngier 进行了深入的技术交流。Fuad 提出了将处理逻辑简化为一个 switch 语句的建议，Marc 对此表示赞同，但也提出了对 EL2 寄存器初始化规则的不确定性，认为需要引入“有效值”的概念来处理未启用 NV (Nested Virtualization) 的情况。此外，Marc 还指出了在 L1 客户机运行于 EL2 时 HCRX_EL2 的适用性问题，认为当前的实现可能存在脆弱性，需进一步思考代码的重构。

总体来看，本周讨论集中在补丁的实现细节和潜在问题上，参与者们积极探讨如何优化代码以确保其在不同虚拟化状态下的可靠性。

#### 📝 邮件列表

1. **[03-04 14:36]** Re: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[03-04 15:25]** Re: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[03-04 15:47]** Re: [PATCH 03/18] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-04 16:55]** Re: [PATCH 07/18] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 14: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 10:12:19 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于移除 `PXD_TABLE_BIT` 的补丁（PATCH V2 0/8），主要涉及 ARM64 架构的内存管理。补丁的目的是去掉 `PXX_TABLE_BIT` 定义，转而依赖于更抽象的 `PXX_TYPE_MASK`、`PXX_TYPE_SECT` 和 `PXX_TYPE_TABLE`，以便为即将到来的 D128 页表支持做好准备。

在历史讨论中，Anshuman Khandual 提出了这一补丁，并解释了其背后的逻辑和必要性。Ryan Roberts 对补丁表示支持，但建议将所有相关修改合并为一个补丁，以便于审查和记录。此建议旨在简化补丁的结构，使其更易于理解。

在本周的新讨论中，Anshuman Khandual 和 Ryan Roberts 继续探讨补丁的结构。Anshuman 表示，虽然他倾向于保持当前的逐步补丁系列，但如果大家达成共识，他可以将大部分补丁合并为一个。Ryan 也同意暂时保持现状，等待其他参与者的意见。

总体而言，讨论围绕补丁的结构和逻辑展开，参与者们在寻求最佳的解决方案，以确保代码的可读性和功能的一致性。

#### 📝 邮件列表

1. **[02-21 10:12]** [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[02-28 15:32]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>
3. **[03-03 10:32]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[03-03 10:23]** Re: [PATCH V2 0/8] arm64/mm: Drop PXD_TABLE_BIT
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>

---

### Thread 15: [PATCH 00/11] Tracefs support for pKVM

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 24 Feb 2025 12:13:42 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于为 pKVM 提供 Tracefs 支持的补丁系列，主要由 Vincent Donnefort 提出。该补丁的目的是为了增强在保护模式下的虚拟机监控器的调试和分析能力，Tracefs 被认为是一个理想的工具，因为它易于使用并且与多种工具兼容。

在历史讨论中，Vincent 提出了一个补丁（PATCH 02/11），旨在将环形缓冲区的数据页面结构和时间戳编码函数移至公共的 `ring_buffer.h` 头文件，以便于外部写入符合环形缓冲区标准的页面。这一改动为后续的功能扩展奠定了基础。

在本周的新讨论中，参与者 Steven Rostedt 对该补丁提出了建议，指出在将内容移至 `include/linux` 目录时，需要添加前缀以防止命名空间冲突，具体提到了 `RB_TS_SHIFT`、`RB_TS_MASK` 和 `RB_TS_DELTA_TEST` 这几个命名。此反馈为补丁的进一步完善提供了方向。

#### 📝 邮件列表

1. **[02-24 12:13]** [PATCH 00/11] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-24 12:13]** [PATCH 02/11] ring-buffer: Expose buffer_data_page material
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[03-06 14:56]** Re: [PATCH 02/11] ring-buffer: Expose buffer_data_page material
   - 发件人: Steven Rostedt <rostedt@goodmis.org>

---

### Thread 16: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 12:13:55 +0000

#### 🤖 AI 总结

本邮件讨论主题为“[PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats”，由 Vincent Donnefort 提出，旨在将 pKVM 在 guest stage-2 中使用的页面计入二级页表统计信息，类似于 VHE 模式的处理。该补丁的目的是提高内存统计的准确性，以便更好地反映 pKVM 的资源使用情况。

在历史讨论中，Vincent 提出了补丁的具体实现，并对其进行了签名。此补丁的背景是为了优化 KVM 在 arm64 架构下的性能和资源管理。

在本周的新讨论中，Oliver Upton 提出了一个问题，询问在 teardown_mc 过程中是否还会清理其他结构（如 vcpu 结构），暗示可能存在更复杂的内存管理情况。Vincent 随后承认确实存在这种情况，并表示他在 Android 分支中留下了一些更改，计划重新整理一个更合适的版本。

总结来看，本周的讨论主要集中在补丁的潜在问题和改进方向上，参与者们对内存管理的复杂性进行了深入探讨。

#### 📝 邮件列表

1. **[02-28 12:13]** [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[03-03 13:18]** Re: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[03-04 09:03]** Re: [PATCH] KVM: arm64: Count pKVM stage-2 usage in secondary
 pagetable stats
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 17: [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 27 Feb 2025 00:33:04 +0000

#### 🤖 AI 总结

本邮件讨论的主题是将 pKVM 所有权状态迁移到 hyp_vmemmap 的补丁系列（PATCH 0/6）。该补丁的主要目标是提高超管的状态查找效率，避免在查找时进行页面表遍历，并且将超管状态与线性映射范围的存在解耦，从而为未来的特性引入（如 hyp 跟踪）简化代码。

在之前的讨论中，Quentin Perret 强调了将超管所有权状态整合到 struct hyp_page 中的优势，包括更高效的查找和增强安全性。这些改动将有助于在不需要映射到线性范围的情况下，跟踪映射到超管私有范围的页面状态。

在本周的新讨论中，Vincent Donnefort 提出了对补丁的疑问，询问在引入“不要在 EL2 映射 'kvm_vgic_global_state'”之后，SHARED_OWNED 和 SHARED_BORROWED 状态是否仍然相关。他指出，在设置时似乎没有任何 !OWNED 页面存在于 hyp 中，暗示可能需要重新评估这些状态的必要性。

总体来看，本周的讨论集中在补丁的有效性和必要性上，尤其是与新引入的机制之间的关系。

#### 📝 邮件列表

1. **[02-27 00:33]** [PATCH 0/6] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-27 00:33]** [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
3. **[03-03 09:47]** Re: [PATCH 4/6] KVM: arm64: Move hyp state to hyp_vmemmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 18: [PATCH] KVM: arm64: Writable TGRAN*_2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Mar 2025 19:40:13 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“可写的 TGRAN*_2”。该补丁的主要目的是允许用户空间写入 ID_AA64MMFR0_EL1 寄存器中的安全（NI）值，同时禁止在非虚拟化（NV）环境中更改这些字段，因为 KVM 提供了基于 PAGE_SIZE 的清理视图。此外，补丁还增加了相关位到 set_id_regs 的自测中。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了增强 KVM 的功能，确保在虚拟化环境中对特定寄存器的访问控制。

本周的新讨论中，Sebastian Ott 提交了补丁，并详细描述了补丁的实现细节，包括对相关代码的修改。Marc Zyngier 对该补丁表示认可，确认了其有效性并给予了支持。这表明该补丁得到了积极的反馈，可能会在未来的版本中被合并。

#### 📝 邮件列表

1. **[03-06 19:40]** [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[03-09 18:24]** Re: [PATCH] KVM: arm64: Writable TGRAN*_2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 14:02:23 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上进行虚拟机实时迁移的错误管理的补丁（PATCH v8 0/6）。该补丁的主要内容是修复了由于 CONFIG_CORESIGHT_SOURCE_ETM4X 配置引起的编译错误，并添加了 R-by 标签，旨在增强 KVM 在处理特定 CPU 实现时的能力。

在历史讨论中，Shameer Kolothum 提到补丁的第八版（v8）相较于第七版（v7）做出了重要的改进，并提供了相关的 QEMU 分支链接以供测试。此外，补丁中包含了多个功能的实现，包括对 MIDR/REVIDR 的内部读取、引入超调用支持、以及基于实现 CPU 启用错误管理等。

在本周的新讨论中，Oliver Upton 表示该补丁已被应用到下一个版本中，并感谢 Shameer 的贡献。他还提供了每个补丁的具体链接，便于参与者查看和测试。这表明该补丁在社区中的接受度较高，且进展顺利。

#### 📝 邮件列表

1. **[02-21 14:02]** [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[03-05 15:58]** Re: [PATCH v8 0/6] KVM: arm64: Errata management for VM Live migration
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 25 Feb 2025 17:29:14 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 arm64 架构添加 NV GICv3 支持的补丁（PATCH v4 00/16）。该补丁旨在增强 GICv3 的支持，以便更好地处理中断和虚拟化相关的任务。

在历史讨论中，Marc Zyngier 提出了该补丁的多个版本（v1 到 v4），并在每个版本中进行了相应的修改和改进。例如，在 v4 中，他增加了关于 L2 到 L1 中断处理优先级的注释，并且基于 Linux 内核 6.14-rc3 进行了重基。之前的版本主要集中在修复默认值和整合来自其他开发者的反馈。

在本周的新讨论中，Oliver Upton 对补丁进行了积极评价，指出整体状态良好，并感谢 Marc 的努力。他确认该补丁已被应用到下一步的开发中，标志着该功能的进一步推进。此外，邮件中列出了补丁的具体内容和链接，涵盖了多个与 GICv3 相关的寄存器和功能的实现。

总的来说，本周的讨论表明该补丁已获得认可并进入下一阶段，显示出开发团队对 GICv3 支持的持续关注和努力。

#### 📝 邮件列表

1. **[02-25 17:29]** [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-03 22:27]** Re: [PATCH v4 00/16] KVM: arm64: Add NV GICv3 support
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 21: [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 02 Mar 2025 17:12:54 +0900

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的性能监控单元（PMU）相关的补丁。补丁的主要内容是修复 SET_ONE_REG 操作在设置 vPMU 计数器（vPMC registers）时的行为，确保在设置 vPMC 寄存器时重置当前的性能事件。这一修改是为了应对之前的补丁（commit 9228b26194d1），该补丁修复了 GET_ONE_REG 操作。

在历史讨论中，Akihiko Odaki 提出了补丁的背景，指出在某些情况下，vPMC 寄存器的值会保存在系统寄存器文件中，但这些保存的值在性能事件计数后并不代表当前的 vPMC 寄存器值。

在本周的新讨论中，Oliver Upton 对补丁提出了一些担忧，特别是关于在虚拟机（VM）启动后更改性能监控计数器可能引发的奇怪情况。他指出，PMU 配置在 KVM_RUN 之前可能会发生变化，这可能导致在恢复虚拟机状态时出现错误。他建议在 vCPU 已经运行过一次后再调用 kvm_pmu_set_counter_value()，否则应更新寄存器的内存值，以确保性能事件与 vPMU 的最终配置相匹配。

#### 📝 邮件列表

1. **[03-02 17:12]** [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Akihiko Odaki <akihiko.odaki@daynix.com>
2. **[03-03 11:26]** Re: [PATCH] KVM: arm64: PMU: Fix SET_ONE_REG for vPMC regs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 21 Feb 2025 17:45:26 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 单元测试库的补丁提案，主题为将 `__ASSEMBLY__` 替换为 `__ASSEMBLER__`。该补丁的主要目的是将所有非 x86 的条件编译指令从 `__ASSEMBLY__` 转换为 `__ASSEMBLER__`，并移除手动定义的 `__ASSEMBLY__`。`__ASSEMBLER__` 是编译器在预处理汇编代码时自动定义的，不需要手动定义，确保代码正常运行，而 `__ASSEMBLY__` 则是从 Linux 内核中继承而来，使用上较为繁琐。

在历史讨论中，Sean Christopherson 提出了该补丁，并指出 `__ASSEMBLY__` 的使用是历史遗留问题，可能并没有实际的必要。

在本周的新讨论中，Thomas Huth 对补丁表示感谢，并询问为何内核使用 `__ASSEMBLY__` 而非 `__ASSEMBLER__`。Sean Christopherson 回复认为这纯粹是历史原因，并未给出明确的技术依据。整体来看，补丁得到了认可，并已应用于代码中，讨论主要集中在历史使用习惯的探讨上。

#### 📝 邮件列表

1. **[02-21 17:45]** [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[03-06 10:00]** Re: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of
 __ASSEMBLY__
   - 发件人: Thomas Huth <thuth@redhat.com>
3. **[03-06 14:17]** Re: [RFC kvm-unit-tests PATCH] lib: Use __ASSEMBLER__ instead of __ASSEMBLY__
   - 发件人: Sean Christopherson <seanjc@google.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.14, take #4

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Mar 2025 16:18:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM/arm64 的修复补丁，旨在解决在 hVHE 模式下 pKVM 的 PSCI 中继实现中的两个相关错误。这些错误导致主机在 MMU 状态不确定的情况下进入，并且 EL2 处于错误模式。

**原始补丁内容**：本次补丁包含两项修复，分别由 Ahmed Genidi 和 Mark Rutland 提交，主要是初始化 SCTLR_EL1 和 HCR_EL2.E2H，以确保在 CPU 初始化时正确设置。

**之前讨论要点**：邮件中没有提及历史讨论内容，说明此次讨论是基于最近的修复需求进行的。

**本周的新讨论与进展**：Marc Zyngier 提交了这组补丁，并请求 Paolo 进行合并。Paolo 在收到补丁后确认已完成合并，表示感谢。这表明补丁得到了及时的审查和接受，预计将会在即将发布的 6.14 版本中生效。

#### 📝 邮件列表

1. **[03-07 16:18]** [GIT PULL] KVM/arm64 fixes for 6.14, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[03-09 09:11]** Re: [GIT PULL] KVM/arm64 fixes for 6.14, take #4
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Other

共 5 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v1 0/7] arm64: support EL2

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 20 Feb 2025 14:13:47 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 arm64 架构的 kvm-unit-tests 的一系列补丁，主要目的是增加对 EL2 的支持。历史讨论中，Joey Gouly 提出了七个补丁，涵盖了如何在 EL2 下运行测试、如何处理定时器和性能监控单元（PMU）等方面的问题。补丁的关键内容包括：在启动时如果处于 EL2 则降级到 EL1、在 EL2 下使用虚拟化定时器、以及在 EL2 下计数周期等。

在之前的讨论中，Alexandru Elisei 对补丁提出了一些建议和问题，主要集中在 EL2 寄存器的初始化和定时器的实现细节上。他对补丁的部分内容表示认可，但也指出了一些需要改进的地方，例如缺少对某些寄存器的断言。

在本周的新讨论中，Joey 和 Alexandru 继续交流补丁的细节。Joey 表示会考虑对 PMU 的某些设置进行调整，并承认在理解 ARM 架构文档时出现了错误。Alexandru 提出了一些具体的代码实现建议，并强调了在缺乏 KVM ABI 的情况下，软件不应依赖于特定实现的寄存器重置值。整体来看，讨论进展顺利，补丁逐步完善。

#### 📝 邮件列表

1. **[02-20 14:13]** [kvm-unit-tests PATCH v1 0/7] arm64: support EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[02-20 14:13]** [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[02-20 14:13]** [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[02-20 14:13]** [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[02-27 16:53]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[02-27 16:55]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[02-27 17:01]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[03-04 16:56]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[03-04 17:02]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[03-04 17:05]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
11. **[03-06 15:52]** Re: [kvm-unit-tests PATCH v1 1/7] arm64: drop to EL1 if booted at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[03-06 15:52]** Re: [kvm-unit-tests PATCH v1 2/7] arm64: timer: use hypervisor
 timers when at EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[03-06 15:58]** Re: [kvm-unit-tests PATCH v1 6/7] arm64: pmu: count EL2 cycles
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 21 Feb 2025 17:27:54 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 RISC-V 架构的 KVM 单元测试的两个补丁，主要目的是允许使用除 'virt' 之外的其他 QEMU 机器模型。

在历史讨论中，Andrew Jones 提出了两个补丁。第一个补丁（PATCH 0/2）允许在命令行中覆盖默认的 'virt' 模型，并支持为早期输出指定不同的 UART 地址。第二个补丁（PATCH 1/2）则是为了使早期控制台（earlycon）能够适用于所有架构，而不仅限于 ARM 架构，直接应用于 RISC-V。

在本周的新讨论中，Andrew Jones 对第一个补丁进行了确认并表示已合并，感谢参与者的贡献。同时，他补充说明将添加对 ARM/ARM64 和 RISC-V32/RISC-V64 的相关说明，因为目前没有其他架构关注该参数。

总体来看，本周的进展主要是补丁的合并和对补丁内容的进一步说明，标志着对 RISC-V 支持的增强。

#### 📝 邮件列表

1. **[02-21 17:27]** [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[02-21 17:27]** [kvm-unit-tests PATCH 1/2] configure: Allow earlycon for all architectures
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
3. **[03-04 10:12]** Re: [kvm-unit-tests PATCH 1/2] configure: Allow earlycon for all
 architectures
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
4. **[03-04 10:31]** Re: [kvm-unit-tests PATCH 0/2] riscv: Run with other QEMU models
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 3: [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Mar 2025 09:39:53 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 单元测试的补丁，主题为“Makefile: 在 cc-option 中使用 CFLAGS”。补丁的主要内容是修改 Makefile，使得在使用 clang 进行交叉编译时，可以在 cc-option 中正确识别目标特定选项。具体而言，补丁在 CC 调用中添加了 CFLAGS，以解决在没有指定 CFLAGS 的情况下，cc-option 无法识别目标特定选项的问题。

在之前的讨论中，Andrew Jones 提出了这个补丁，并解释了其必要性。Thomas Huth 对该补丁进行了审核，并表示支持。

本周的新讨论中，Thomas Huth 对补丁表示感谢，但随后指出补丁存在问题，导致 x86 构建失败，出现了递归变量引用错误。Andrew Jones 随后承认了这个问题，并表示将会修复该错误并提交一个新的版本（v2）。整体来看，虽然补丁初步得到了支持，但由于存在缺陷，仍需进一步修改。

#### 📝 邮件列表

1. **[03-07 09:39]** [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
2. **[03-07 09:42]** Re: [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option
   - 发件人: Thomas Huth <thuth@redhat.com>
3. **[03-07 09:45]** Re: [kvm-unit-tests PATCH] Makefile: Use CFLAGS in cc-option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 4: writable ID_AA64MMFR0_EL1.TGRAN*_2 ?

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Feb 2025 16:19:06 +0100 (CET)

#### 🤖 AI 总结

在本次邮件讨论中，主题为“writable ID_AA64MMFR0_EL1.TGRAN*_2”的问题主要涉及在两个Graviton主机之间迁移时，ID寄存器中TGRAN*_2的可写性。历史讨论中，Sebastian Ott提出了这个问题，指出当前两个主机在S2支持的大小上存在差异，且TGRAN*_2寄存器尚不可写。他建议可以将这些寄存器的客人视图设置为NI（不适用），或者允许在两种值之间转换，并可能允许写入NI。

在本周的新讨论中，Marc Zyngier回应了Sebastian的提议，认为在非NV（非虚拟化）上下文中，可以允许对任何TGRAN*_2寄存器写入任何值。然而，对于NV上下文，他强调必须严格控制，确保NI是该功能的最低限制，不能允许写入0值。

总结来说，讨论围绕如何处理TGRAN*_2寄存器的可写性展开，历史讨论提出了初步建议，而本周的讨论则进一步明确了在不同上下文中的处理原则。

#### 📝 邮件列表

1. **[02-28 16:19]** writable ID_AA64MMFR0_EL1.TGRAN*_2 ?
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[03-03 19:39]** Re: writable ID_AA64MMFR0_EL1.TGRAN*_2 ?
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 5: [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  7 Mar 2025 10:18:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 单元测试的 Makefile 修改，主要由 Andrew Jones 提出。原始的 patch 旨在改进 Makefile 中的 cc-option 函数，使其在使用 Clang 进行交叉编译时能够正确识别目标特定的选项。具体来说，patch 增加了 CFLAGS 到 CC 调用中，以避免在编译 x86 时出现错误。

在之前的讨论中，未提及具体的历史背景或其他相关 patch，因此本周的讨论是该主题的首次提出。Andrew Jones 在本周的邮件中详细描述了 patch 的内容，并指出引入 realmode_bits 变量是为了防止在构建 x86 时由于 CFLAGS 自我引用而导致的构建失败。

本周的进展包括对 patch 的修正，确保 x86 构建能够正常进行。具体修改涉及 Makefile 和 x86/Makefile.common 文件的更改，增加了必要的代码行以支持新的编译选项。整体来看，本周的讨论集中在确保 KVM 单元测试的构建过程更加稳定和兼容性上。

#### 📝 邮件列表

1. **[03-07 10:18]** [kvm-unit-tests PATCH v2] Makefile: Use CFLAGS in cc-option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

