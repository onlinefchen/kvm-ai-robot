# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 10:32:19

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 238
- **总 Thread 数**: 23
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 19 threads (209 邮件)
- **RFC**: 2 threads (15 邮件)
- **Other**: 2 threads (14 邮件)

---

## 📌 PATCH

共 19 个 thread

---

### Thread 1: [PATCH v3 01/10] arm/cpu: Add infra to handle generated ID
 register definitions

**📧 邮件数**: 27 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 13 May 2025 15:52:56 +0200

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM 架构的补丁（PATCH v3 01/10），旨在添加处理生成的 ID 寄存器定义的基础设施。该补丁的背景是为了改进 KVM（内核虚拟机）对 ARM 处理器的支持，特别是在 ID 寄存器的管理和自定义方面。

在历史讨论中，参与者们提出了对补丁的初步反馈，包括对术语的使用、数据类型的建议，以及对注释的需求，以便更清晰地解释不同类型的索引和寄存器的功能。

本周的新讨论中，参与者们继续对补丁进行细化和改进，Eric Auger 和 Cornelia Huck 提出了多个建议，包括重命名某些定义以更好地与 KVM API 关联，增加注释以提高代码可读性，以及讨论如何处理寄存器的可写性和默认值的变化。Daniel Berrangé 还提到，GPL-2.0 许可证的使用需要更新为更合适的 SPDX 标识符。此外，Shameerali Kolothum Thodi 表示将会在完成当前补丁系列后，继续开发与 QEMU 集成的支持。

总体而言，本周的讨论集中在补丁的细节优化和代码风格的一致性上，参与者们积极提出建议，以确保补丁的功能性和可维护性。

#### 📝 邮件列表

1. **[05-13 15:52]** Re: [PATCH v3 01/10] arm/cpu: Add infra to handle generated ID
 register definitions
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[05-13 16:05]** Re: [PATCH v3 01/10] arm/cpu: Add infra to handle generated ID
 register definitions
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[05-13 16:20]** Re: [PATCH v3 04/10] kvm: kvm_get_writable_id_regs
   - 发件人: Eric Auger <eric.auger@redhat.com>
4. **[05-13 16:31]** Re: [PATCH v3 06/10] arm/kvm: Allow reading all the writable ID
 registers
   - 发件人: Eric Auger <eric.auger@redhat.com>
5. **[05-13 16:33]** Re: [PATCH v3 07/10] arm/kvm: write back modified ID regs to KVM
   - 发件人: Eric Auger <eric.auger@redhat.com>
6. **[05-13 16:42]** Re: [PATCH v3 04/10] kvm: kvm_get_writable_id_regs
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[05-13 16:47]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host cpu
 model
   - 发件人: Eric Auger <eric.auger@redhat.com>
8. **[05-13 16:50]** Re: [PATCH v3 09/10] arm-qmp-cmds: introspection for ID register
 props
   - 发件人: Eric Auger <eric.auger@redhat.com>
9. **[05-13 17:09]** Re: [PATCH v3 10/10] arm/cpu-features: document ID reg properties
   - 发件人: Eric Auger <eric.auger@redhat.com>
10. **[05-13 17:12]** Re: [PATCH v3 01/10] arm/cpu: Add infra to handle generated ID
 register definitions
   - 发件人: Eric Auger <eric.auger@redhat.com>
11. **[05-13 17:16]** Re: [PATCH v3 04/10] kvm: kvm_get_writable_id_regs
   - 发件人: Eric Auger <eric.auger@redhat.com>
12. **[05-13 16:23]** Re: [PATCH v3 02/10] arm/cpu: Add sysreg properties generation
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
13. **[05-13 17:29]** Re: [PATCH v3 00/10] kvm/arm: Introduce a customizable aarch64 KVM
 host model
   - 发件人: Eric Auger <eric.auger@redhat.com>
14. **[05-13 16:56]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
15. **[05-13 16:59]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
16. **[05-13 17:23]** Re: [PATCH v3 10/10] arm/cpu-features: document ID reg properties
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
17. **[05-14 13:47]** RE: [PATCH v3 00/10] kvm/arm: Introduce a customizable aarch64 KVM
 host model
   - 发件人: Shameerali Kolothum Thodi <shameerali.kolothum.thodi@huawei.com>
18. **[05-14 16:47]** Re: [PATCH v3 00/10] kvm/arm: Introduce a customizable aarch64 KVM
 host model
   - 发件人: Eric Auger <eric.auger@redhat.com>
19. **[05-14 17:25]** Re: [PATCH v3 02/10] arm/cpu: Add sysreg properties generation
   - 发件人: Cornelia Huck <cohuck@redhat.com>
20. **[05-14 16:29]** Re: [PATCH v3 02/10] arm/cpu: Add sysreg properties generation
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
21. **[05-14 17:36]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Cornelia Huck <cohuck@redhat.com>
22. **[05-14 19:22]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
23. **[05-16 16:17]** Re: [PATCH v3 06/10] arm/kvm: Allow reading all the writable ID
 registers
   - 发件人: Cornelia Huck <cohuck@redhat.com>
24. **[05-16 16:42]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Cornelia Huck <cohuck@redhat.com>
25. **[05-16 16:51]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Cornelia Huck <cohuck@redhat.com>
26. **[05-16 15:57]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
27. **[05-16 17:13]** Re: [PATCH v3 08/10] arm/cpu: more customization for the kvm host
 cpu model
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 2: [PATCH v5 00/25] Tracefs support for pKVM

**📧 邮件数**: 26 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 16 May 2025 14:40:06 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 pKVM 的 Tracefs 支持的补丁系列（[PATCH v5 00/25]），主要内容包括引入新的远程事件和简单环形缓冲区的实现，以便在保护模式下进行调试和性能分析。

1. **原始补丁/问题内容**：
   该补丁系列旨在为 pKVM 超级管理程序提供 Tracefs 支持，允许在保护模式下记录和读取事件。补丁包括创建远程事件、环形缓冲区的实现，以及与 Tracefs 的集成。

2. **之前讨论要点**：
   之前的讨论集中在如何实现远程事件和环形缓冲区的高效交互，以及如何确保内核和超管之间的数据共享。补丁的设计考虑了 Tracefs 的易用性和与现有工具的兼容性。

3. **本周的新讨论、进展或结论**：
   - 本周的邮件中，Vincent Donnefort 提出了多个补丁，逐步实现了环形缓冲区的远程支持、事件的创建和管理、以及 Tracefs 接口的整合。
   - 具体进展包括引入简单环形缓冲区的实现、添加事件支持、以及为 pKVM 超级管理程序创建 Tracefs 目录结构。
   - 还讨论了如何在 Tracefs 中实现对事件的读取和控制，确保在 pKVM 中能够有效地记录和分析事件。
   - 最后，补丁还包括对 pKVM 自测试事件的支持，确保新功能的正确性和稳定性。

整体来看，这一系列补丁为 pKVM 的调试和性能分析提供了重要的基础设施，增强了其在保护模式下的可观察性。

#### 📝 邮件列表

1. **[05-16 14:40]** [PATCH v5 00/25] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[05-16 14:40]** [PATCH v5 01/25] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[05-16 14:40]** [PATCH v5 02/25] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[05-16 14:40]** [PATCH v5 03/25] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[05-16 14:40]** [PATCH v5 04/25] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[05-16 14:40]** [PATCH v5 05/25] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[05-16 14:40]** [PATCH v5 06/25] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[05-16 14:40]** [PATCH v5 07/25] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[05-16 14:40]** [PATCH v5 08/25] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[05-16 14:40]** [PATCH v5 09/25] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[05-16 14:40]** [PATCH v5 10/25] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[05-16 14:40]** [PATCH v5 11/25] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[05-16 14:40]** [PATCH v5 12/25] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[05-16 14:40]** [PATCH v5 13/25] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[05-16 14:40]** [PATCH v5 14/25] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[05-16 14:40]** [PATCH v5 15/25] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[05-16 14:40]** [PATCH v5 16/25] KVM: arm64: Add .hyp.data section
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[05-16 14:40]** [PATCH v5 17/25] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[05-16 14:40]** [PATCH v5 18/25] KVM: arm64: Add tracing capability for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[05-16 14:40]** [PATCH v5 19/25] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[05-16 14:40]** [PATCH v5 20/25] KVM: arm64: Sync boot clock with the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[05-16 14:40]** [PATCH v5 21/25] KVM: arm64: Add trace reset to the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[05-16 14:40]** [PATCH v5 22/25] KVM: arm64: Add event support to the pKVM hyp and
 trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[05-16 14:40]** [PATCH v5 23/25] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[05-16 14:40]** [PATCH v5 24/25] KVM: arm64: Add selftest event support to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[05-16 14:40]** [PATCH v5 25/25] tracing: selftests: Add pKVM trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 3: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit

**📧 邮件数**: 20 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 30 Apr 2025 21:55:05 +1000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 RME（Realm Management Extensions）功能的补丁，特别是关于处理 realm 进入和退出的实现（PATCH v8 16/43）。

**原始补丁内容**：该补丁旨在增强 KVM（Kernel-based Virtual Machine）对 ARM64 架构的支持，具体涉及 realm 的进入和退出操作的处理。

**历史讨论要点**：在之前的讨论中，参与者对补丁的细节进行了审查，提出了多个小的改进建议。例如，Gavin Shan 提到了一些代码逻辑的优化建议，并对函数返回值的处理提出了看法。Suzuki K Poulose 也对补丁的某些实现提出了审查意见，强调了需要处理的边界情况。

**本周新讨论进展**：本周的讨论中，Steven Price 针对补丁的实现进行了进一步的修改和优化，特别是在处理 kvm_exit 跟踪和 RTT（Realm Translation Table）管理方面。他考虑了是否在 kvm_exit 中提供伪造的程序计数器（PC）值，并最终决定在没有实际用例的情况下不引入新的跟踪方式。此外，Emi Kisanuki 提供了对补丁的测试反馈，确认在其内部模拟器中成功启动了 realm 虚拟机，并通过了大部分测试。这些进展表明补丁在实际应用中的有效性和稳定性。

总体来看，邮件讨论围绕补丁的细节优化和实际测试结果展开，显示出社区对 ARM64 RME 功能的持续关注和改进。

#### 📝 邮件列表

1. **[04-30 21:55]** Re: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Gavin Shan <gshan@redhat.com>
2. **[04-30 22:11]** Re: [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Gavin Shan <gshan@redhat.com>
3. **[05-01 10:16]** Re: [PATCH v8 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
4. **[05-02 10:46]** Re: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>
5. **[05-02 12:04]** Re: [PATCH v8 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[05-06 14:23]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[05-07 11:26]** Re: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[05-07 11:42]** Re: [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
9. **[05-12 15:44]** Re: [PATCH v8 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
10. **[05-12 15:45]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
11. **[05-12 15:45]** Re: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
12. **[05-12 15:45]** Re: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
13. **[05-13 11:43]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
14. **[05-14 11:24]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
15. **[05-15 03:01]** RE: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
16. **[05-16 14:50]** Re: [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
17. **[05-16 14:50]** Re: [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
18. **[05-16 16:33]** Re: [PATCH v8 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
19. **[05-16 16:57]** Re: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
20. **[05-16 17:00]** Re: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 4: [PATCH v4 00/17] KVM: arm64: Recursive NV support

**📧 邮件数**: 18 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 14 May 2025 11:34:43 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对递归虚拟化（Recursive NV）支持的补丁集（PATCH v4 00/17）。该补丁集的核心在于实现 VNCR_EL2（Virtual Nested Context Register）功能，以支持嵌套虚拟化。

在历史讨论中，Marc Zyngier 提到，VNCR 的虚拟化意味着 L1 虚拟机需要为 L2 准备 VNCR 页面，并在 L0 上进行映射。这一过程涉及到页面的管理和 TLB（Translation Lookaside Buffer）的处理。补丁集的目标是确保在合适的时机拥有正确的页面，并且能够处理各种可能导致页面不可访问的情况。

本周的新讨论中，Marc Zyngier 提出了多个补丁，逐步实现了 VNCR_EL2 的功能，包括：
1. 添加 VNCR_EL2 的布局和分配页面的逻辑。
2. 提取地址转换的辅助函数，以支持 VNCR_EL2 的访问。
3. 处理 VNCR_EL2 触发的故障，并实现对 VNCR_EL2 的映射。
4. 处理 TLB 无效化，确保在进行 TLB 无效化时能够正确处理 VNCR 的映射。

此外，补丁集还增加了对用户空间的支持，使其能够请求 KVM_ARM_VCPU_EL2 功能，标志着对嵌套虚拟化的支持趋于完整。整体来看，这一系列补丁的实施将极大增强 KVM 在 arm64 架构下的虚拟化能力。

#### 📝 邮件列表

1. **[05-14 11:34]** [PATCH v4 00/17] KVM: arm64: Recursive NV support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[05-14 11:34]** [PATCH v4 01/17] arm64: sysreg: Add layout for VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-14 11:34]** [PATCH v4 02/17] KVM: arm64: nv: Allocate VNCR page when required
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[05-14 11:34]** [PATCH v4 03/17] KVM: arm64: nv: Extract translation helper from the AT code
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[05-14 11:34]** [PATCH v4 04/17] KVM: arm64: nv: Snapshot S1 ASID tagging information during walk
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[05-14 11:34]** [PATCH v4 05/17] KVM: arm64: nv: Move TLBI range decoding to a helper
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[05-14 11:34]** [PATCH v4 06/17] KVM: arm64: nv: Don't adjust PSTATE.M when L2 is nesting
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-14 11:34]** [PATCH v4 07/17] KVM: arm64: nv: Add pseudo-TLB backing VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[05-14 11:34]** [PATCH v4 08/17] KVM: arm64: nv: Add userspace and guest handling of VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[05-14 11:34]** [PATCH v4 09/17] KVM: arm64: nv: Handle VNCR_EL2-triggered faults
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[05-14 11:34]** [PATCH v4 10/17] KVM: arm64: nv: Handle mapping of VNCR_EL2 at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[05-14 11:34]** [PATCH v4 11/17] KVM: arm64: nv: Handle VNCR_EL2 invalidation from MMU notifiers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[05-14 11:34]** [PATCH v4 12/17] KVM: arm64: nv: Program host's VNCR_EL2 to the fixmap address
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[05-14 11:34]** [PATCH v4 13/17] KVM: arm64: nv: Add S1 TLB invalidation primitive for VNCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[05-14 11:34]** [PATCH v4 14/17] KVM: arm64: nv: Plumb TLBI S1E2 into system instruction dispatch
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[05-14 11:34]** [PATCH v4 15/17] KVM: arm64: nv: Remove dead code from ERET handling
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[05-14 11:34]** [PATCH v4 16/17] KVM: arm64: Allow userspace to request KVM_ARM_VCPU_EL2*
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[05-14 11:35]** [PATCH v4 17/17] KVM: arm64: Document NV caps and vcpu flags
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 5: [PATCH v4 00/10] Stage-2 huge mappings for pKVM np-guests

**📧 邮件数**: 17 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  9 May 2025 14:16:56 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于为 pKVM 非特权虚拟机（np-guests）实现二级大页映射的补丁系列。该补丁系列旨在支持在 stage-2 中安装 PMD 级别的映射，特别是在 stage-1 由 Hugetlbfs 或透明大页（THPs）支持的情况下。

在历史讨论中，Vincent Donnefort 提出了多个补丁，涉及到处理大页映射的函数、引入遍历辅助函数、以及为 __pkvm_host_share_guest() 添加范围参数等。这些补丁的目标是优化在 pKVM 中的内存管理，确保在支持大页映射时的性能提升。

在本周的新讨论中，Marc Zyngier 对多个补丁提出了具体的改进建议，包括确保地址和大小对齐、改进迭代器的实现、以及对 PxD 命名法的质疑。他强调了代码的安全性和可维护性，建议在实现中加入更多的边界检查和未来兼容性考虑。Vincent Donnefort 对这些反馈表示感谢，并表示愿意进行相应的修改，以确保代码的健壮性和可读性。

整体来看，本周的讨论集中在对补丁的细节优化和代码安全性提升上，参与者们积极交流，推动补丁的完善。

#### 📝 邮件列表

1. **[05-09 14:16]** [PATCH v4 00/10] Stage-2 huge mappings for pKVM np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[05-09 14:16]** [PATCH v4 01/10] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[05-09 14:16]** [PATCH v4 02/10] KVM: arm64: Introduce for_each_hyp_page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[05-09 14:16]** [PATCH v4 03/10] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[05-09 14:17]** [PATCH v4 07/10] KVM: arm64: Convert pkvm_mappings to interval tree
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[05-09 14:17]** [PATCH v4 09/10] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[05-09 14:17]** [PATCH v4 10/10] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[05-16 13:15]** Re: [PATCH v4 01/10] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[05-16 13:57]** Re: [PATCH v4 02/10] KVM: arm64: Introduce for_each_hyp_page
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[05-16 14:10]** Re: [PATCH v4 03/10] KVM: arm64: Add a range to __pkvm_host_share_guest()
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[05-16 14:15]** Re: [PATCH v4 07/10] KVM: arm64: Convert pkvm_mappings to interval tree
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[05-16 14:28]** Re: [PATCH v4 09/10] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[05-16 14:55]** Re: [PATCH v4 10/10] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[05-16 18:53]** Re: [PATCH v4 01/10] KVM: arm64: Handle huge mappings for np-guest
 CMOs
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[05-16 19:03]** Re: [PATCH v4 10/10] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[05-17 09:51]** Re: [PATCH v4 01/10] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[05-17 09:53]** Re: [PATCH v4 10/10] KVM: arm64: np-guest CMOs with PMD_SIZE fixmap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v7 00/14] arm: rework id register storage

**📧 邮件数**: 15 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 15 May 2025 17:38:53 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM 架构的 ID 寄存器存储的重构，主要集中在一系列补丁（PATCH v7 00/14 至 14/14）的提交和修改。以下是讨论的主要内容：

1. **原始补丁/问题内容**：补丁系列旨在重构 ARM 架构的 ID 寄存器存储方式，主要通过将寄存器定义从结构体转移到数组中，以便更好地支持 KVM 和其他功能。

2. **之前讨论要点**：在历史讨论中，补丁经历了多次迭代，修复了之前版本中的一些问题，如缺失的 SPDX 标识、代码重构以及对寄存器定义的生成进行了优化。参与者们对补丁的可读性和可维护性进行了讨论，确保代码在不同版本的 Linux 内核中都能正常工作。

3. **本周的新讨论和进展**：本周的讨论中，补丁继续得到审查和修改，新增了自动生成系统寄存器定义的脚本，以便从 Linux 源代码中提取寄存器信息。此脚本的引入旨在简化寄存器定义的维护工作。此外，补丁中还改进了对 KVM 的支持，确保在不同的寄存器访问中使用更简洁的代码结构。

总体而言，本线程的讨论集中在提高 ARM ID 寄存器的存储效率和代码的可维护性上，参与者们积极反馈和修改补丁，确保其在未来的开发中能够更好地适应 ARM 架构的需求。

#### 📝 邮件列表

1. **[05-15 17:38]** [PATCH v7 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[05-15 17:38]** [PATCH v7 01/14] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[05-15 17:38]** [PATCH v7 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[05-15 17:38]** [PATCH v7 03/14] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[05-15 17:38]** [PATCH v7 04/14] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[05-15 17:38]** [PATCH v7 05/14] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[05-15 17:38]** [PATCH v7 06/14] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[05-15 17:39]** [PATCH v7 07/14] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[05-15 17:39]** [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[05-15 17:39]** [PATCH v7 09/14] arm/cpu: Store id_pfr0/1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[05-15 17:39]** [PATCH v7 10/14] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[05-15 17:39]** [PATCH v7 11/14] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[05-15 17:39]** [PATCH v7 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[05-15 17:39]** [PATCH v7 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[05-15 17:39]** [PATCH v7 14/14] arm/kvm: use fd instead of fdarray[2]
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 7: [PATCH v4 5/5] KVM: arm64: vgic-its: Clear ITE when DISCARD frees an ITE

**📧 邮件数**: 14 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 12 May 2025 14:09:09 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的多个补丁和问题，主要集中在虚拟化和内存管理方面。

1. **原始补丁内容**：
   - 主题为“[PATCH v4 5/5] KVM: arm64: vgic-its: Clear ITE when DISCARD frees an ITE”，该补丁旨在确保在执行 DISCARD 命令时，清除 ITE（Interrupt Translation Entry）以避免潜在的内存错误。

2. **之前讨论要点**：
   - 在本周的讨论中，David Sauerwein 提到在应用该补丁后，某些虚拟机出现了空指针解引用的问题，怀疑是由于竞争条件导致的。Marc Zyngier 对此表示怀疑，认为 KVM 不会在非保存/恢复事件中使用来宾内存。

3. **本周的新讨论与进展**：
   - David 提出了对问题的分析，并尝试通过锁定读取来解决，但未能成功。Marc 则要求提供更详细的来宾堆栈跟踪以进一步分析问题。
   - 此外，Per Larsen 提交了一系列补丁，涉及 FF-A 1.2 规范的支持，包括对新消息接口的实现和对现有功能的改进，确保 KVM 在处理虚拟机时能够正确管理缓存和内存映射。

综上所述，本周的讨论围绕着补丁的潜在问题和新功能的实现展开，显示出开发者们对 KVM 在 arm64 架构下的稳定性和性能的持续关注。

#### 📝 邮件列表

1. **[05-12 14:09]** Re: [PATCH v4 5/5] KVM: arm64: vgic-its: Clear ITE when DISCARD frees an ITE
   - 发件人: David Sauerwein <dssauerw@amazon.de>
2. **[05-16 10:52]** Re: [PATCH v4 5/5] KVM: arm64: vgic-its: Clear ITE when DISCARD frees an ITE
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-16 12:13]** [PATCH v4 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[05-16 12:14]** [PATCH v4 1/5] KVM: arm64: Restrict FF-A host version
 renegotiation
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[05-16 12:14]** [PATCH v4 2/5] KVM: arm64: Zero x4-x7 in ffa_set_retval
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[05-16 12:14]** [PATCH v4 3/5] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[05-16 12:14]** [PATCH v4 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
8. **[05-16 12:14]** [PATCH v4 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
9. **[05-18 05:47]** [PATCH v4 0/5] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
10. **[05-18 05:47]** [PATCH v4 1/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
11. **[05-18 05:47]** [PATCH v4 2/5] KVM: arm64: Make stage2_has_fwb global scope
   - 发件人: ankita <ankita@nvidia.com>
12. **[05-18 05:47]** [PATCH v4 3/5] kvm: arm64: New memslot flag to indicate cacheable mapping
   - 发件人: ankita <ankita@nvidia.com>
13. **[05-18 05:47]** [PATCH v4 4/5] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
14. **[05-18 05:47]** [PATCH v4 5/5] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>

---

### Thread 8: [PATCH v6 00/14] arm: rework id register storage

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  6 May 2025 10:52:20 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM 架构的 ID 寄存器存储重构的补丁系列（[PATCH v6 00/14]）。该补丁主要目的是改进 ARM 处理器的 ID 寄存器存储方式，包括修复之前版本中的一些转换错误，并增加了 KVM 访问器以存储主机特性。

在历史讨论中，Cornelia Huck 提出了多个补丁，涉及到 ID 寄存器的存储、系统寄存器生成脚本的引入等。Eric Auger 和其他参与者对补丁进行了审查，并提出了一些建议和修改意见，确保补丁的质量和功能。

本周的新讨论中，Eric Auger 和 Cornelia Huck 对补丁系列表示认可，认为没有发现新的转换问题。Daniel Berrangé 提出了一些关于补丁的细节问题，如变量的移除时机和许可证名称的有效性，并建议将补丁更新到 v7 版本，期待这是最后一次迭代。总体来看，讨论进展顺利，补丁系列得到了积极的反馈，预计将进入最终审查阶段。

#### 📝 邮件列表

1. **[05-06 10:52]** [PATCH v6 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[05-06 10:52]** [PATCH v6 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[05-06 10:52]** [PATCH v6 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[05-06 10:52]** [PATCH v6 14/14] arm/kvm: use fd instead of fdarray[2]
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[05-13 11:35]** Re: [PATCH v6 14/14] arm/kvm: use fd instead of fdarray[2]
   - 发件人: Eric Auger <eric.auger@redhat.com>
6. **[05-13 11:38]** Re: [PATCH v6 00/14] arm: rework id register storage
   - 发件人: Eric Auger <eric.auger@redhat.com>
7. **[05-13 11:57]** Re: [PATCH v6 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[05-13 17:11]** Re: [PATCH v6 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
9. **[05-13 17:15]** Re: [PATCH v6 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
10. **[05-14 16:54]** Re: [PATCH v6 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[05-14 16:55]** Re: [PATCH v6 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[05-14 17:01]** Re: [PATCH v6 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Eric Auger <eric.auger@redhat.com>
13. **[05-14 16:26]** Re: [PATCH v6 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>

---

### Thread 9: [PATCH v5 0/6] KVM: lockdep improvements

**📧 邮件数**: 11 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 12 May 2025 14:04:01 -0400

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）的锁依赖性（lockdep）改进，主要集中在一系列补丁（PATCH v5 0/6）上。

**原始补丁内容**：
补丁的核心是实现了使用 lockdep 的“嵌套锁”（nest_lock）特性，以改进 KVM 中对所有虚拟 CPU（vCPUs）的锁定方式。通过添加 `mutex_trylock_nest_lock()` 和 `mutex_lock_killable_nest_lock()` 函数，补丁旨在消除 SEV 代码中的自定义解决方案，并解决 ARM 和 RISC-V 代码中出现的锁依赖性警告。

**之前讨论要点**：
在之前的讨论中，开发者们提到 KVM 在处理大量 vCPUs 时，lockdep 无法有效管理同一类锁的同时锁定，导致锁深度超限的警告。通过引入嵌套锁特性，可以在持有其他锁的情况下安全地锁定多个 vCPUs，从而避免这些警告。

**本周新讨论和进展**：
本周的讨论集中在补丁的具体实现上，包括新增的 `kvm_lock_all_vcpus()` 和 `kvm_trylock_all_vcpus()` 函数的使用。这些函数被替换了之前的自定义实现，确保在锁定所有 vCPUs 时不会触发 lockdep 警告。参与者们对补丁进行了测试和审核，得到了多个开发者的认可（如 Anup Patel 和 Marc Zyngier 的确认），并建议将其合并到稳定分支中，以便在未来的版本中使用。整体来看，本周的讨论推动了补丁的进一步完善和应用。

#### 📝 邮件列表

1. **[05-12 14:04]** [PATCH v5 0/6] KVM: lockdep improvements
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
2. **[05-12 14:04]** [PATCH v5 1/6] locking/mutex: implement mutex_trylock_nested
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
3. **[05-12 14:04]** [PATCH v5 2/6] locking/mutex: implement mutex_lock_killable_nest_lock
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
4. **[05-12 14:04]** [PATCH v5 3/6] KVM: add kvm_lock_all_vcpus and kvm_trylock_all_vcpus
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
5. **[05-12 14:04]** [PATCH v5 4/6] x86: KVM: SVM: use kvm_lock_all_vcpus instead of a custom implementation
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
6. **[05-12 14:04]** [PATCH v5 5/6] KVM: arm64: use kvm_trylock_all_vcpus when locking all vCPUs
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
7. **[05-12 14:04]** [PATCH v5 6/6] RISC-V: KVM: use kvm_trylock_all_vcpus when locking all vCPUs
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
8. **[05-13 16:48]** Re: [PATCH v5 6/6] RISC-V: KVM: use kvm_trylock_all_vcpus when
 locking all vCPUs
   - 发件人: Anup Patel <anup@brainfault.org>
9. **[05-13 13:45]** Re: [PATCH v5 0/6] KVM: lockdep improvements
   - 发件人: Peter Zijlstra <peterz@infradead.org>
10. **[05-14 10:33]** Re: [PATCH v5 3/6] KVM: add kvm_lock_all_vcpus and kvm_trylock_all_vcpus
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[05-14 10:35]** Re: [PATCH v5 5/6] KVM: arm64: use kvm_trylock_all_vcpus when locking all vCPUs
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 10: [PATCH 0/3] KVM: arm64: Address Translation fixes

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 14 May 2025 10:47:48 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的地址转换修复和 vGICv4（虚拟通用中断控制器版本4）配置的相关补丁。

1. **原始补丁内容**：本次补丁包括三个部分，主要修复了 KVM 在地址转换中的一些问题，确保在 AT S1E* 上正确报告 PAR_EL1.{PTW,S}，处理访问故障，并防止将未初始化的数据传递给 HCR_EL2。

2. **之前讨论要点**：历史讨论中没有具体提到，但补丁的背景是为了增强 KVM 在处理虚拟机中断时的灵活性，特别是在支持 vGICv4 的情况下。

3. **本周的新讨论与进展**：本周的讨论主要集中在 vGICv4 的配置上。Raghavendra Rao Ananta 提出了一个新的属性 KVM_DEV_ARM_VGIC_CONFIG_GICV4，允许用户空间为特定虚拟机启用或禁用 vGICv4。Marc Zyngier 表示已将补丁应用到下一个版本中。Ben Horgan 提出了对当前设计的质疑，认为在某些情况下，禁用 vGICv4 的命令行参数可能过于严格。Raghavendra 回应说，当前设计确保了在系统启动时对 vGICv4 的可用性做出承诺，以避免潜在的硬件问题。

总体来看，本周的讨论推动了对 vGICv4 配置的深入理解和修正，确保在不同虚拟机环境中能够灵活处理中断。

#### 📝 邮件列表

1. **[05-14 10:47]** Re: [PATCH 0/3] KVM: arm64: Address Translation fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[05-14 19:21]** [PATCH 0/3] KVM: arm64: Allow vGICv4 configuration per VM
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[05-14 19:21]** [PATCH 1/3] kvm: arm64: Add support for KVM_DEV_ARM_VGIC_CONFIG_GICV4 attr
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[05-14 19:21]** [PATCH 2/3] docs: kvm: devices/arm-vgic-v3: Document
 KVM_DEV_ARM_VGIC_CONFIG_GICV4 attr
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
5. **[05-14 19:21]** [PATCH 3/3] KVM: selftests: Extend vgic_init to test GICv4 config attr
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
6. **[05-15 11:30]** Re: [PATCH 0/3] KVM: arm64: Allow vGICv4 configuration per VM
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[05-15 11:48]** Re: [PATCH 0/3] KVM: arm64: Allow vGICv4 configuration per VM
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-15 08:55]** Re: [PATCH 0/3] KVM: arm64: Allow vGICv4 configuration per VM
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
9. **[05-15 17:48]** Re: [PATCH 0/3] KVM: arm64: Allow vGICv4 configuration per VM
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

### Thread 11: [PATCH v1 0/6] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  5 May 2025 16:14:06 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）处理 ARM 架构下的同步外部中止（SEA）的问题，主要通过一系列补丁来改进现有的处理机制。

1. **原始补丁内容**：Jiaqi Yan 提出的补丁系列（共6个补丁）旨在改进 KVM 在处理 VCPU 遇到 SEA 时的行为。目前，当主机的 APEI 无法处理阶段2的中止时，KVM 会直接注入一个异步 SError，导致虚拟机内核崩溃。补丁的目标是提供一种更优雅的处理方式，允许用户空间在处理 SEA 时有更多的控制。

2. **之前讨论要点**：历史讨论中，补丁的各个部分逐步阐述了如何在不同情况下处理 SEA，包括如何设置 VCPU 的状态寄存器以反映错误状态，以及如何记录和文档化新的用户空间 API。这些讨论强调了在现代数据中心环境中，处理可恢复的内存错误的重要性。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的细节上。Jiaqi Yan 感谢 Alok Tiwari 指出补丁中的拼写错误，并表示已将这些修正纳入 V2 版本。同时，Marc Zyngier 对补丁的某些实现细节提出了疑问，认为某些信息不应在提交信息中包含，并建议将部分代码与现有的 MMU 代码合并。讨论中还涉及到如何处理不同情况下的错误报告，以及用户空间对虚拟地址的关注程度。

总体来看，邮件讨论围绕如何优化 KVM 对 SEA 的处理展开，强调了在虚拟化环境中实现更高效和安全的错误处理机制的重要性。

#### 📝 邮件列表

1. **[05-05 16:14]** [PATCH v1 0/6] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[05-05 16:14]** [PATCH v1 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[05-05 16:14]** [PATCH v1 2/6] KVM: arm64: Set FnV for VCPU when FAR_EL2 is invalid
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[05-05 16:14]** [PATCH v1 6/6] Documentation: kvm: new uAPI for handling SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[05-08 00:54]** Re: [PATCH v1 6/6] Documentation: kvm: new uAPI for handling SEA
   - 发件人: ALOK TIWARI <alok.a.tiwari@oracle.com>
6. **[05-14 14:29]** Re: [PATCH v1 6/6] Documentation: kvm: new uAPI for handling SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
7. **[05-16 16:20]** Re: [PATCH v1 1/6] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-16 16:33]** Re: [PATCH v1 2/6] KVM: arm64: Set FnV for VCPU when FAR_EL2 is invalid
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH v3 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 13 May 2025 06:28:29 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 及其新的 SEND_DIRECT2 ABI 的补丁集（PATCH v3 0/3）。该补丁集的主要目的是确保主机不会使用低于已与虚拟机监控器（hypervisor）协商的 FF-A 版本，以避免兼容性问题。

在历史讨论中，补丁集的背景是 FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。补丁集的核心内容包括对 SMCCC 1.2 的支持以及对未实现的 FF-A 1.2 接口的处理。

本周的新讨论中，参与者 Per Larsen 提交了三个补丁，分别是：
1. **PATCH v3 1/3**：限制主机版本重新协商，确保一旦协商版本后不允许降级，修复了当前行为以返回 NOT_SUPPORTED。
2. **PATCH v3 2/3**：将支持的 FF-A 版本提升至 1.2，并更新相关函数以支持新的接口。
3. **PATCH v3 3/3**：在主机处理程序中支持 FFA_MSG_SEND_DIRECT_REQ2，利用 SMCCC v1.2 调用约定。

此外，Will Deacon 对补丁提出了一些建议和修改意见，主要集中在代码的安全性和逻辑清晰性上，表示对补丁的认可并提出了进一步的改进建议。整体来看，讨论围绕着实现 FF-A 1.2 的技术细节及其对现有系统的影响展开。

#### 📝 邮件列表

1. **[05-13 06:28]** [PATCH v3 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[05-13 06:28]** [PATCH v3 1/3] KVM: arm64: Restrict FF-A host version
 renegotiation
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[05-13 06:28]** [PATCH v3 2/3] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[05-13 06:28]** [PATCH v3 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[05-13 15:21]** Re: [PATCH v3 1/3] KVM: arm64: Restrict FF-A host version
 renegotiation
   - 发件人: Will Deacon <will@kernel.org>
6. **[05-13 15:56]** Re: [PATCH v3 2/3] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Will Deacon <will@kernel.org>
7. **[05-15 17:46]** Re: [PATCH v3 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 13: [PATCH v4 00/24] Tracefs support for pKVM

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  6 May 2025 17:47:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了关于为 pKVM 添加 Tracefs 支持的补丁（PATCH v4 00/24）。该补丁旨在为保护模式下的虚拟化提供调试和分析工具，Tracefs 被认为是一个理想的选择，因为它易于使用并且与多种工具兼容。

在历史讨论中，Vincent Donnefort 提出了补丁的初步版本，并详细介绍了其功能和设计思路。Steven Rostedt 对补丁中的某个结构体大小提出了疑问，认为应该将其调整为 30 以避免内存对齐问题。

在本周的新讨论中，Vincent 和 Steven 继续探讨补丁的构建问题。Steven 报告了构建失败的错误，并提出了可能的解决方案，包括对模块文件的管理和函数导出问题。Vincent 表示他已经在本地修复了一些问题，并计划在本周提交补丁的 v5 版本。尽管 Vincent 将于周末休假，但他鼓励 Steven 在此期间继续推进补丁的修改。

总体来看，讨论集中在补丁的具体实现和构建问题上，参与者们积极协作以推动项目进展。

#### 📝 邮件列表

1. **[05-06 17:47]** [PATCH v4 00/24] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[05-06 17:48]** [PATCH v4 05/24] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[05-09 15:47]** Re: [PATCH v4 05/24] tracing: Add events to trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
4. **[05-12 08:55]** Re: [PATCH v4 05/24] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[05-14 13:38]** Re: [PATCH v4 00/24] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
6. **[05-14 19:13]** Re: [PATCH v4 00/24] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[05-14 14:28]** Re: [PATCH v4 00/24] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>

---

### Thread 14: [PATCH v4 00/43] KVM: arm64: Revamp Fine Grained Trap handling

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  6 May 2025 17:43:05 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的细粒度陷阱处理（Fine Grained Trap handling）进行重构的补丁系列（PATCH v4 00/43）。Marc Zyngier 提出了这一系列补丁，主要目的是优化和扩展对 FGT2 及其依赖项的支持。

在历史讨论中，Marc 提到该补丁系列自上一个版本以来，规模几乎翻倍，包含了更多的补丁和代码变更，强调了尽快合并或放弃的紧迫性。他还详细描述了补丁的变更日志，包括对 CPACR_EL 中缺失位域的补充和对 FGT2 寄存器的清理。

在本周的新讨论中，参与者 Joey Gouly 对两个具体补丁进行了审查，分别是补丁 33（使用 FGT 特性映射来驱动 RES0 位）和补丁 38（为 FEAT_FGT2 寄存器添加清理）。他表示对补丁的修改是合理的，并给予了“已审查通过”的反馈，表明这些补丁在功能上是可接受的。

总体来看，本周的讨论主要集中在对补丁的审查和确认上，标志着这一系列补丁在社区中的逐步推进。

#### 📝 邮件列表

1. **[05-06 17:43]** [PATCH v4 00/43] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[05-06 17:43]** [PATCH v4 33/43] KVM: arm64: Use FGT feature maps to drive RES0 bits
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-06 17:43]** [PATCH v4 38/43] KVM: arm64: Add sanitisation for FEAT_FGT2 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[05-15 16:24]** Re: [PATCH v4 33/43] KVM: arm64: Use FGT feature maps to drive RES0
 bits
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[05-15 17:04]** Re: [PATCH v4 38/43] KVM: arm64: Add sanitisation for FEAT_FGT2
 registers
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 15: [PATCH 00/10] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 06 May 2025 12:41:32 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Armv8.8 SPE（采样和性能监控扩展）特性的补丁，主要由 James Clark 提出。补丁内容包括支持三项新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性是独立的，可以单独应用。补丁分为多个部分，包括系统寄存器的更改和性能工具的调整。

在历史讨论中，James Clark 提出了补丁的具体内容，并详细说明了每个特性的实现方式及其与现有性能监控工具的兼容性。特别是，前两项特性可以与旧版性能监控工具一起使用，而最后一项特性则需要对工具进行更新以解析新的配置。

在本周的新讨论中，Marc Zyngier 对补丁的某些部分进行了回应，提到这些特性在 JSON 文件中被描述为枚举类型，进一步确认了补丁的细节。这表明讨论仍在继续，参与者对补丁的具体实现和文档化进行了深入探讨。

#### 📝 邮件列表

1. **[05-06 12:41]** [PATCH 00/10] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[05-06 12:41]** [PATCH 01/10] arm64: sysreg: Add new PMSIDR_EL1 and PMSFCR_EL1
 fields
   - 发件人: James Clark <james.clark@linaro.org>
3. **[05-16 15:38]** Re: [PATCH 01/10] arm64: sysreg: Add new PMSIDR_EL1 and PMSFCR_EL1 fields
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v3] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  8 May 2025 14:00:09 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 AmpereOne AC04 处理器的 erratum AC04_CPU_23 的补丁（PATCH v3），旨在解决在特定情况下更新 HCR_EL2 时可能导致的数据地址翻译错误。补丁建议在对 HCR_EL2 进行存储操作前执行 DSB 指令，以防止旧指令在错误窗口内执行，并在存储后执行 ISB 指令，以防止新指令的影响。

在历史讨论中，D Scott Phillips 提出了该补丁，并详细解释了问题的根源和解决方案。Oliver Upton 对补丁进行了初步审核，指出需要在文档中添加相关条目，以确保补丁的完整性。

在本周的新讨论中，D Scott Phillips 对 Oliver Upton 提出的文档缺失问题表示歉意，并承诺将进行修正。这表明补丁的审核过程仍在进行中，且开发者们在积极沟通以确保补丁的完善。整体来看，讨论进展顺利，补丁即将完善并提交。

#### 📝 邮件列表

1. **[05-08 14:00]** [PATCH v3] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
2. **[05-09 03:08]** Re: [PATCH v3] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[05-13 11:42]** Re: [PATCH v3] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>

---

### Thread 17: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0 into
 the idregs arrays

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 13 May 2025 16:41:06 +0100

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是一个针对 ARM 架构的补丁（PATCH），其目的是将 `aa64isar0` 和 `aa64zfr0` 寄存器存储到 ID 寄存器数组中。该补丁的版本为 v5。

在之前的讨论中，尚未提及具体的历史背景或问题，但本周的讨论揭示了补丁在构建时遇到的问题。参与者 Daniel 指出，当 KVM 功能被禁用或在构建目标架构上不可用时，补丁会导致构建失败，具体错误信息涉及到对 `CONFIG_KVM` 的使用被标记为“毒化”（poisoned），从而导致编译中断。

Cornelia Huck 随后回应，表示她已经在 v6 版本中修复了这个问题，并确认她在测试时使用的是 v5 版本，因为该版本可以与 KVM CPU 模型系列兼容。

总的来说，本周的讨论主要集中在补丁的构建问题及其修复进展上，参与者们积极沟通以解决技术障碍。

#### 📝 邮件列表

1. **[05-13 16:41]** Re: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0 into
 the idregs arrays
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
2. **[05-13 17:56]** Re: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0
 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[05-13 17:17]** Re: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0 into
 the idregs arrays
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>

---

### Thread 18: [PATCH] KVM: arm64: nv: Remove clearing of ICH_LR<n>.EOI if ICH_LR<n>.HW == 1

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 12 May 2025 21:32:23 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“移除在 ICH_LR<n>.HW == 1 时清除 ICH_LR<n>.EOI 的操作”。该补丁的目的是在 ICH_LR<n>.HW 为 1 的情况下，避免不必要的清除操作，因为此时 EOI（End of Interrupt）位并不具有实际意义，且后续的清除操作会自动将相关位清零。

在本周的讨论中，Wei-Lin Chang 提出了该补丁，并解释了其逻辑和目的，强调没有功能上的变化。补丁的具体修改包括在 `vgic-v3-nested.c` 文件中删除了三行代码，这些代码原本用于清除 EOI 位。随后，Marc Zyngier 对该补丁表示认可，并确认已将其应用到下一步的开发中。

总结而言，本周的讨论主要集中在该补丁的合理性和必要性上，最终得到了积极的反馈并被采纳。

#### 📝 邮件列表

1. **[05-12 21:32]** [PATCH] KVM: arm64: nv: Remove clearing of ICH_LR<n>.EOI if ICH_LR<n>.HW == 1
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[05-16 13:06]** Re: [PATCH] KVM: arm64: nv: Remove clearing of ICH_LR<n>.EOI if ICH_LR<n>.HW == 1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH v4] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 13 May 2025 11:45:14 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对AmpereOne AC04处理器的错误修复补丁，具体是针对其错误AC04_CPU_23的解决方案。该错误可能导致在执行加载/存储指令时，HCR_EL2的更新会偶尔破坏数据地址的同时翻译。为了解决这个问题，补丁提出在写入HCR_EL2之前添加一个数据同步屏障（DSB），并在之后添加一个指令同步屏障（ISB），以防止指令在错误窗口内执行。

在历史讨论中，补丁经历了多个版本的修改，主要集中在确保错误修复的有效性和代码的整洁性。每个版本都对补丁进行了细微的调整，例如在补丁中添加了新的帮助函数，确保在汇编文件中正确处理HCR_EL2的存储。

本周的新讨论中，补丁的最新版本（v4）已经得到审核，并且在文档中增加了对该错误的描述。补丁的实现涉及到对多个文件的修改，包括Kconfig和相关的汇编代码，确保在不同情况下都能正确应用该错误修复。整体来看，该补丁的推进显示了对AmpereOne AC04处理器稳定性的持续关注和改进。

#### 📝 邮件列表

1. **[05-13 11:45]** [PATCH v4] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 12 May 2025 03:52:42 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构上启用嵌套虚拟化（Nested Virtualization，NV）自测的补丁系列（RFC PATCH v2 0/9）。该补丁系列的主要内容是修改现有的自测代码，使其能够在 NV 启用的情况下运行。

**原始问题/补丁内容**：
该补丁系列的目标是使自测能够在启用 NV 的情况下正常工作，具体是将来宾代码在 vEL2（虚拟扩展级别2）中运行，而不是默认的 EL1。补丁中包含了对大约12个自测案例的修改，并添加了命令行选项以启用 NV 测试，默认情况下这些测试是禁用的。

**之前讨论要点**：
在之前的讨论中，开发者对补丁的设计和实现提出了一些反馈，主要集中在如何更好地支持 NV 的功能和确保测试的有效性。

**本周新讨论及进展**：
本周的讨论中，Ganapatrao Kulkarni 提交了补丁的多个版本，包括：
1. 对 vEL2 运行环境的支持。
2. 添加了简单的测试案例来验证在 NV 启用情况下的功能。
3. 扩展了对定时器、VGIC（虚拟通用中断控制器）等的测试支持。
4. 进行了多项自测的修改，以确保在 NV 启用时能够正确执行。

每个补丁都详细描述了所做的修改和新增的测试案例，确保了在不同情况下的兼容性和功能验证。整体来看，本周的讨论推动了 KVM 在 ARM64 架构上嵌套虚拟化自测的进一步完善。

#### 📝 邮件列表

1. **[05-12 03:52]** [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[05-12 03:52]** [RFC PATCH v2 1/9] KVM: arm64: nv: selftests: Add support to run guest code in vEL2.
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
3. **[05-12 03:52]** [RFC PATCH v2 2/9] KVM: arm64: nv: selftests: Add simple test to run guest code in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
4. **[05-12 03:52]** [RFC PATCH v2 3/9] KVM: arm64: nv: selftests: Enable hypervisor timer tests to run in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
5. **[05-12 03:52]** [RFC PATCH v2 4/9] KVM: arm64: nv: selftests: enable aarch32_id_regs test to run in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
6. **[05-12 03:52]** [RFC PATCH v2 5/9] KVM: arm64: nv: selftests: Enable vgic tests to run in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
7. **[05-12 03:52]** [RFC PATCH v2 6/9] KVM: arm64: nv: selftests: Enable set_id_regs test to run in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
8. **[05-12 03:52]** [RFC PATCH v2 7/9] KVM: arm64: nv: selftests: Enable test to run in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
9. **[05-12 03:52]** [RFC PATCH v2 8/9] KVM: selftests: arm64: Extend kvm_page_table_test to run guest code in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
10. **[05-12 03:52]** [RFC PATCH v2 9/9] KVM: arm64: nv: selftests: Enable page_fault_test test to run in vEL2
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>

---

### Thread 2: [RFC PATCH v2 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 12 May 2025 12:41:09 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 在 arm64 架构下如何处理 MTE（Memory Tagging Extension）功能的补丁。原始补丁旨在解决一个问题，即在不支持 MTE_ASYNC 的情况下，错误地向虚拟机报告该功能为可用。补丁的核心是暴露 MTE_frac 字段，以确保虚拟机能正确识别 MTE 的支持情况。

在历史讨论中，补丁的背景是当前 KVM 隐藏了 ID_AA64PFR1_EL1.MTE_frac 字段，导致在某些情况下虚拟机错误地认为 MTE_ASYNC 是支持的。Linux 内核并未检查 MTE_frac 字段，假设只要支持 MTE，就可以生成 MTE 异步故障。

在本周的新讨论中，Ben Horgan 提出了三个补丁，分别是：
1. 暴露 MTE_frac 字段，使其对 KVM 可见。
2. 使 MTE_frac 的掩码条件依赖于 MTE 功能的实际支持情况。
3. 添加自测以确认暴露 MTE_frac 不会影响迁移功能。

最终，Marc Zyngier 表示已将这些补丁应用到下一步开发中，确认了补丁的有效性和必要性。这些补丁的实施将改善 KVM 对 MTE 功能的处理，确保虚拟机能够准确反映主机的硬件支持情况。

#### 📝 邮件列表

1. **[05-12 12:41]** [RFC PATCH v2 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[05-12 12:41]** [RFC PATCH v2 1/3] arm64/sysreg: Expose MTE_frac so that it is visible to KVM
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[05-12 12:41]** [RFC PATCH v2 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[05-12 12:41]** [RFC PATCH v2 3/3] KVM: selftests: Confirm exposing MTE_frac does not break migration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[05-16 13:04]** Re: [RFC PATCH v2 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v3 00/16] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  7 May 2025 16:12:40 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于在 KVM 单元测试中添加 kvmtool 支持的补丁系列（PATCH v3 00/16）。该补丁的主要目标是允许用户通过简单的命令配置和运行所有测试，特别是针对 ARM 和 ARM64 架构。kvmtool 相较于 QEMU 更小且易于修改，适合开发者在添加或原型设计新特性时使用。

在历史讨论中，Alexandru Elisei 提出了多个补丁，主要包括：
1. 将 `extra_params` 重命名为 `qemu_params`，以支持 kvmtool 的不同语法。
2. 添加 `test_args` 参数，以便于传递与虚拟机管理器无关的测试参数。
3. 更新 `run_tests.sh` 脚本以记录新参数，并确保在未配置为使用 kvmtool 时拒绝运行测试。

在本周的新讨论中，Shaoqin Huang 对所有补丁进行了审核，并给予了“Reviewed-by”标记，表明这些补丁已获得认可并准备进入下一步。整体来看，讨论进展顺利，补丁系列得到了积极的反馈，预计将推动 kvmtool 支持的实现。

#### 📝 邮件列表

1. **[05-07 16:12]** [kvm-unit-tests PATCH v3 00/16] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[05-07 16:12]** [kvm-unit-tests PATCH v3 01/16] scripts: unittests.cfg: Rename 'extra_params' to 'qemu_params'
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[05-07 16:12]** [kvm-unit-tests PATCH v3 02/16] scripts: Add 'test_args' test definition parameter
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[05-07 16:12]** [kvm-unit-tests PATCH v3 04/16] run_tests.sh: Document --probe-maxsmp argument
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[05-07 16:12]** [kvm-unit-tests PATCH v3 05/16] scripts: Document environment variables
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[05-07 16:12]** [kvm-unit-tests PATCH v3 06/16] scripts: Refuse to run the tests if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[05-07 16:12]** [kvm-unit-tests PATCH v3 07/16] scripts: Use an associative array for qemu argument names
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[05-14 10:57]** Re: [kvm-unit-tests PATCH v3 01/16] scripts: unittests.cfg: Rename
 'extra_params' to 'qemu_params'
   - 发件人: Shaoqin Huang <shahuang@redhat.com>
9. **[05-14 11:16]** Re: [kvm-unit-tests PATCH v3 02/16] scripts: Add 'test_args' test
 definition parameter
   - 发件人: Shaoqin Huang <shahuang@redhat.com>
10. **[05-14 11:29]** Re: [kvm-unit-tests PATCH v3 04/16] run_tests.sh: Document
 --probe-maxsmp argument
   - 发件人: Shaoqin Huang <shahuang@redhat.com>
11. **[05-14 11:36]** Re: [kvm-unit-tests PATCH v3 05/16] scripts: Document environment
 variables
   - 发件人: Shaoqin Huang <shahuang@redhat.com>
12. **[05-14 15:49]** Re: [kvm-unit-tests PATCH v3 06/16] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Shaoqin Huang <shahuang@redhat.com>
13. **[05-14 16:02]** Re: [kvm-unit-tests PATCH v3 07/16] scripts: Use an associative array
 for qemu argument names
   - 发件人: Shaoqin Huang <shahuang@redhat.com>

---

### Thread 2: [syzbot] [kvmarm?] KASAN: invalid-access Read in kvm_vgic_set_owner

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 12 May 2025 09:46:24 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KASAN（Kernel Address Sanitizer）在 `kvm_vgic_set_owner` 函数中发现的无效访问问题。该问题由 syzbot 提交，涉及到 ARM64 架构的 KVM 虚拟化。

在本周的讨论中，syzbot 报告了一个内核错误，具体表现为在执行 `kvm_vgic_set_owner` 时发生了无效内存访问，导致内核崩溃。错误信息显示，内核在尝试读取一个无效地址时触发了 KASAN 报告，提示可能存在野指针访问。报告中包含了详细的调用栈和相关的内存地址信息，但目前尚未提供可重现该问题的测试用例。

此次讨论没有涉及历史讨论部分，所有信息均为本周新讨论的内容。syzbot 提醒开发者在修复该问题时，需在提交的补丁中添加特定的标签以便追踪。整体来看，此问题的解决仍需进一步的分析和开发者的介入。

#### 📝 邮件列表

1. **[05-12 09:46]** [syzbot] [kvmarm?] KASAN: invalid-access Read in kvm_vgic_set_owner
   - 发件人: syzbot <syzbot+9993ad918a0b1c0af91c@syzkaller.appspotmail.com>

---

