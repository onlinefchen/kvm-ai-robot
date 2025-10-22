# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 11:22:37

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 173
- **总 Thread 数**: 28
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 23 threads (164 邮件)
- **Selftest**: 1 threads (2 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 3 threads (5 邮件)

---

## 📌 PATCH

共 23 个 thread

---

### Thread 1: [PATCH v7 00/28] Tracefs support for pKVM

**📧 邮件数**: 29 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  3 Oct 2025 14:37:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（PATCH v7 00/28），主要集中在为 pKVM 超级管理程序引入调试和性能分析工具。以下是讨论的主要内容：

1. **原始补丁/问题内容**：
   该补丁系列旨在通过引入 Tracefs 支持，增强 pKVM 超级管理程序的调试和分析能力。Tracefs 提供了一种简单易用的接口，允许用户空间工具访问内核和超级管理程序之间的跟踪事件。

2. **之前讨论要点**：
   之前的版本（v6）主要集中在如何实现远程事件和缓冲区的支持，讨论了如何通过新的接口创建远程事件和缓冲区。补丁中还提到了一些限制和改进点，如非消耗性读取和元页面的同步。

3. **本周的新讨论、进展或结论**：
   本周的讨论主要围绕补丁的具体实现，包括：
   - 引入简单的环形缓冲区实现，以便在 pKVM 中使用。
   - 增加了对事件的支持，允许在超级管理程序中记录和读取事件。
   - 讨论了如何在 Tracefs 中注册和管理这些事件。
   - 提供了自测试模块，以验证新功能的正确性。
   - 讨论了如何在 pKVM 中实现时钟同步和跟踪能力。

整体而言，该补丁系列的目标是通过 Tracefs 提供一个强大的调试和分析工具，以便在 pKVM 环境中更好地监控和管理虚拟化性能。

#### 📝 邮件列表

1. **[10-03 14:37]** [PATCH v7 00/28] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[10-03 14:37]** [PATCH v7 01/28] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[10-03 14:37]** [PATCH v7 02/28] ring-buffer: Store bpage pointers into subbuf_ids
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[10-03 14:38]** [PATCH v7 03/28] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[10-03 14:38]** [PATCH v7 04/28] ring-buffer: Add non-consuming read for ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[10-03 14:38]** [PATCH v7 05/28] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[10-03 14:38]** [PATCH v7 06/28] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[10-03 14:38]** [PATCH v7 07/28] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[10-03 14:38]** [PATCH v7 08/28] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[10-03 14:38]** [PATCH v7 09/28] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[10-03 14:38]** [PATCH v7 10/28] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[10-03 14:38]** [PATCH v7 11/28] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[10-03 14:38]** [PATCH v7 12/28] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[10-03 14:38]** [PATCH v7 13/28] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[10-03 14:38]** [PATCH v7 14/28] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[10-03 14:38]** [PATCH v7 15/28] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[10-03 14:38]** [PATCH v7 16/28] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[10-03 14:38]** [PATCH v7 17/28] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[10-03 14:38]** [PATCH v7 18/28] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[10-03 14:38]** [PATCH v7 19/28] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[10-03 14:38]** [PATCH v7 20/28] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[10-03 14:38]** [PATCH v7 21/28] KVM: arm64: Add tracing capability for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[10-03 14:38]** [PATCH v7 22/28] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[10-03 14:38]** [PATCH v7 23/28] KVM: arm64: Sync boot clock with the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[10-03 14:38]** [PATCH v7 24/28] KVM: arm64: Add trace reset to the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[10-03 14:38]** [PATCH v7 25/28] KVM: arm64: Add event support to the pKVM hyp and
 trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
27. **[10-03 14:38]** [PATCH v7 26/28] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
28. **[10-03 14:38]** [PATCH v7 27/28] KVM: arm64: Add selftest event support to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[10-03 14:38]** [PATCH v7 28/28] tracing: selftests: Add pKVM trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 2: [PATCH 00/13] KVM: arm64: De-specialise the timer UAPI

**📧 邮件数**: 22 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 29 Sep 2025 17:04:44 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要目的是去专门化定时器的用户空间接口（UAPI）。

1. **原始补丁/问题内容**：
   本系列补丁的核心是修复 KVM/arm64 中定时器寄存器的用户空间访问问题。由于定时器寄存器在用户空间访问时未按照正常的系统寄存器流程处理，导致了复杂性和代码重复。补丁旨在将定时器寄存器的处理转移到通用基础设施中，并解决了与寄存器编码交换相关的错误。

2. **之前讨论要点**：
   在历史讨论中，Marc Zyngier 提到定时器寄存器的处理存在多个问题，包括对 nVHE（非虚拟化高效）客户机的寄存器暴露不当，以及用户空间对 CNTV_CVAL_EL0 和 CNTVCT_EL0 的编码交换问题。补丁系列的目标是简化这些处理并提高代码的可维护性。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Marc Zyngier 提出了多个补丁，逐步实现了定时器寄存器的通用化处理。补丁包括隐藏不应暴露给用户空间的寄存器、引入新的帮助函数、以及将定时器上下文指针替换为定时器 ID。此外，Oliver Upton 对某些补丁提出了建议和评论，强调了在处理用户空间接口时需谨慎，避免引入新的问题。整体来看，补丁系列得到了积极的反馈，并逐步朝着简化和修复的方向推进。

#### 📝 邮件列表

1. **[09-29 17:04]** [PATCH 00/13] KVM: arm64: De-specialise the timer UAPI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-29 17:04]** [PATCH 01/13] KVM: arm64: Hide CNTHV_*_EL2 from userspace for nVHE guests
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-29 17:04]** [PATCH 02/13] KVM: arm64: Introduce timer_context_to_vcpu() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-29 17:04]** [PATCH 03/13] KVM: arm64: Replace timer context vcpu pointer with timer_id
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-29 17:04]** [PATCH 04/13] KVM: arm64: Make timer_set_offset() generally accessible
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-29 17:04]** [PATCH 05/13] KVM: arm64: Add timer UAPI workaround to sysreg infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[09-29 17:04]** [PATCH 06/13] KVM: arm64: Move CNT*_CTL_EL0 userspace accessors to generic infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[09-29 17:04]** [PATCH 07/13] KVM: arm64: Move CNT*_CVAL_EL0 userspace accessors to generic infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[09-29 17:04]** [PATCH 08/13] KVM: arm64: Move CNT*CT_EL0 userspace accessors to generic infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[09-29 17:04]** [PATCH 09/13] KVM: arm64: Fix WFxT handling of nested virt
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[09-29 17:04]** [PATCH 10/13] KVM: arm64: Kill leftovers of ad-hoc timer userspace access
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[09-29 17:04]** [PATCH 11/13] KVM: arm64: selftests: Make dependencies on VHE-specific registers explicit
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[09-29 17:04]** [PATCH 12/13] KVM: arm64: selftests: Add an E2H=0-specific configuration to get_reg_list
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[09-29 17:04]** [PATCH 13/13] KVM: arm64: selftest: Fix misleading comment about virtual timer encoding
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[09-29 17:35]** Re: [PATCH 01/13] KVM: arm64: Hide CNTHV_*_EL2 from userspace for
 nVHE guests
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[09-29 17:41]** Re: [PATCH 05/13] KVM: arm64: Add timer UAPI workaround to sysreg
 infrastructure
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
17. **[09-30 08:44]** Re: [PATCH 01/13] KVM: arm64: Hide CNTHV_*_EL2 from userspace for nVHE guests
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[09-30 08:48]** Re: [PATCH 05/13] KVM: arm64: Add timer UAPI workaround to sysreg infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[09-30 11:13]** Re: [PATCH 03/13] KVM: arm64: Replace timer context vcpu pointer
 with timer_id
   - 发件人: Joey Gouly <joey.gouly@arm.com>
20. **[09-30 11:45]** Re: [PATCH 08/13] KVM: arm64: Move CNT*CT_EL0 userspace accessors to
 generic infrastructure
   - 发件人: Joey Gouly <joey.gouly@arm.com>
21. **[09-30 13:05]** Re: [PATCH 08/13] KVM: arm64: Move CNT*CT_EL0 userspace accessors to generic infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[09-30 13:41]** Re: [PATCH 08/13] KVM: arm64: Move CNT*CT_EL0 userspace accessors to
 generic infrastructure
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 3: [PATCH kvmtool 00/15] arm64: Handle PSCI calls in userspace

**📧 邮件数**: 18 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 30 Sep 2025 11:31:14 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 工具的补丁系列，主题为“arm64: 在用户空间处理 PSCI 调用”。该补丁系列的主要目标是实现 ARM 的电源状态和协调接口（PSCI）功能，以便在用户空间中处理相关调用。

**原始补丁/问题内容**：
补丁系列的版本为 v4，主要包括对 PSCI 调用的实现，涉及 CPU 的挂起、开机、亲和性信息等功能。补丁的作者是 Oliver Upton，Suzuki K Poulose 进行了后续的修改和更新。

**之前讨论要点**：
在之前的讨论中，补丁的版本经历了多次修改，主要集中在解决竞态条件、更新头文件以及确保代码与最新的 Linux 内核版本兼容。补丁的功能主要是为了增强 KVM 工具的能力，使其能够更好地支持 ARM 架构的虚拟化。

**本周的新讨论、进展或结论**：
本周的讨论中，Suzuki K Poulose 提交了多个补丁，涵盖了 PSCI 的多个功能实现，包括 CPU_SUSPEND、CPU_ON、AFFINITY_INFO 和 SYSTEM_{OFF,RESET} 等。此外，补丁还引入了 SMCCC 过滤器，以便将 PSCI 调用转发到用户空间处理。最后，Suzuki 提到之前的一封邮件中有重复的补丁，已进行修正。

总体来看，本周的讨论和补丁提交标志着对 KVM 工具在 ARM64 架构上支持 PSCI 的进一步完善，推动了虚拟化功能的增强。

#### 📝 邮件列表

1. **[09-30 11:31]** [PATCH kvmtool 00/15] arm64: Handle PSCI calls in userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
2. **[09-30 11:31]** [PATCH kvmtool v4 01/15] Allow pausing the VM from vcpu thread
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
3. **[09-30 11:31]** [PATCH kvmtool v4 02/15] update_headers: arm64: Track psci.h for PSCI definitions
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
4. **[09-30 11:31]** [PATCH kvmtool v4 03/15] update headers: Linux v6.17-rc7
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
5. **[09-30 11:31]** [PATCH kvmtool v4 04/15] Import arm-smccc.h from Linux 6.16-rc1
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[09-30 11:31]** [PATCH kvmtool v4 04/15] Import arm-smccc.h from Linux 6.17-rc7
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[09-30 11:31]** [PATCH kvmtool v4 05/15] arm64: Stash kvm_vcpu_init for later use
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[09-30 11:31]** [PATCH kvmtool v4 06/15] arm64: Use KVM_SET_MP_STATE ioctl to power off non-boot vCPUs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
9. **[09-30 11:31]** [PATCH kvmtool v4 07/15] arm64: Expose ARM64_CORE_REG() for general use
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
10. **[09-30 11:31]** [PATCH kvmtool v4 08/15] arm64: Add support for finding vCPU for given MPIDR
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
11. **[09-30 11:31]** [PATCH kvmtool v4 09/15] arm64: Add skeleton implementation for PSCI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
12. **[09-30 11:31]** [PATCH kvmtool v4 10/15] arm64: psci: Implement CPU_SUSPEND
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[09-30 11:31]** [PATCH kvmtool v4 11/15] arm64: psci: Implement CPU_ON
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
14. **[09-30 11:31]** [PATCH kvmtool v4 12/15] arm64: psci: Implement AFFINITY_INFO
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
15. **[09-30 11:31]** [PATCH kvmtool v4 13/15] arm64: psci: Implement MIGRATE_INFO_TYPE
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
16. **[09-30 11:31]** [PATCH kvmtool v4 14/15] arm64: psci: Implement SYSTEM_{OFF,RESET}
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
17. **[09-30 11:31]** [PATCH kvmtool v4 15/15] arm64: smccc: Start sending PSCI to userspace
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
18. **[09-30 11:37]** Re: [PATCH kvmtool v4 04/15] Import arm-smccc.h from Linux 6.16-rc1
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 4: [PATCH v10 03/43] arm64: RME: Add SMC definitions for calling the RMM

**📧 邮件数**: 17 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 01 Oct 2025 11:05:00 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM64 RME（Realm Management Extension）的补丁，主要是为调用 RMM（Realm Management Monitor）添加 SMC（Secure Monitor Call）定义。补丁的目标是提升 KVM（Kernel-based Virtual Machine）与 RMM 之间的交互。

在历史讨论中，参与者们探讨了 KVM 如何处理 RMM 的状态，以及 RMM 对 GIC（Generic Interrupt Controller）寄存器的管理。Marc Zyngier 提出了 RMM 不应干预 KVM 的中断处理，而 Steven Price 则认为 RMM 需要控制某些寄存器以确保安全性。

本周的新讨论中，Marc 和 Steven 继续就补丁的细节进行深入交流。Marc 强调 RMM 需要对陷阱行为进行控制，以保护其自身，而 Steven 则质疑这种设计的合理性，认为主机应当完全掌控中断注入。此外，Steven 提出了对用户空间与 RMM 接口的设计意见，认为不应将 RMM 的接口暴露给用户空间，以避免复杂性和潜在问题。

总体而言，讨论围绕 RMM 与 KVM 的交互、寄存器管理及接口设计展开，参与者们对补丁的具体实现和设计理念提出了不同的看法和建议。

#### 📝 邮件列表

1. **[10-01 11:05]** Re: [PATCH v10 03/43] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-01 12:00]** Re: [PATCH v10 03/43] arm64: RME: Add SMC definitions for calling the
 RMM
   - 发件人: Steven Price <steven.price@arm.com>
3. **[10-01 12:05]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[10-01 12:58]** Re: [PATCH v10 03/43] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[10-01 13:28]** Re: [PATCH v10 06/43] arm64: RME: Define the user ABI
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[10-01 14:11]** Re: [PATCH v10 08/43] kvm: arm64: Don't expose debug capabilities for realm guests
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[10-01 14:20]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
8. **[10-01 14:35]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[10-01 14:50]** Re: [PATCH v10 09/43] KVM: arm64: Allow passing machine type in KVM creation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[10-01 15:05]** Re: [PATCH v10 03/43] arm64: RME: Add SMC definitions for calling the
 RMM
   - 发件人: Steven Price <steven.price@arm.com>
11. **[10-01 15:44]** Re: [PATCH v10 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
12. **[10-01 16:19]** Re: [PATCH v10 08/43] kvm: arm64: Don't expose debug capabilities for
 realm guests
   - 发件人: Steven Price <steven.price@arm.com>
13. **[10-01 16:34]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
14. **[10-01 16:36]** Re: [PATCH v10 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[10-01 16:54]** Re: [PATCH v10 09/43] KVM: arm64: Allow passing machine type in KVM
 creation
   - 发件人: Steven Price <steven.price@arm.com>
16. **[10-02 09:46]** Re: [PATCH v10 06/43] arm64: RME: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
17. **[10-02 10:35]** Re: [PATCH v10 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 5: [PATCH v3 0/9] KVM Selftest Runner

**📧 邮件数**: 16 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 30 Sep 2025 09:36:26 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM 自测运行器的第三版补丁（PATCH v3），该补丁系列由 Vipin Sharma 提交，旨在增强 KVM 自测的执行能力。补丁从最初的 15 个减少到 9 个，整合了之前版本的反馈。

### 原始补丁内容
KVM 自测运行器允许用户以更灵活的方式运行 KVM 自测，提供了多种配置选项，如输出控制、并行执行等。补丁的主要目标是简化测试的执行过程，提高测试覆盖率。

### 之前讨论要点
在之前的版本中，讨论集中在如何改善自测运行器的功能，包括自动生成默认测试、支持不同的命令行参数、输出到文件系统等。参与者对如何处理测试结果、输出格式和并行执行提出了建议。

### 本周新讨论与进展
本周的讨论中，Vipin 提交了多个补丁，增加了新的功能：
1. **输出目录选项**：允许用户指定输出目录以保存测试结果。
2. **超时选项**：为测试设置执行时间限制，超时后会标记为“超时”状态。
3. **并行执行**：增加了并发执行测试的能力，用户可以指定同时运行的测试数量。
4. **打印选项**：用户可以选择性地控制不同测试状态的输出内容。
5. **状态显示**：在执行过程中显示当前测试状态的统计信息。
6. **生成默认测试规则**：在 Makefile 中添加规则以自动生成默认测试用例。

此外，Vipin 还更新了 README 文件，详细说明了如何使用自测运行器及其配置选项。参与者对补丁提出了建议，强调了需要遵循现有的构建输出指令。整体来看，讨论围绕如何提升 KVM 自测运行器的灵活性和可用性展开，旨在为开发者提供更好的测试工具。

#### 📝 邮件列表

1. **[09-30 09:36]** [PATCH v3 0/9] KVM Selftest Runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
2. **[09-30 09:36]** [PATCH v3 1/9] KVM: selftest: Create KVM selftest runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
3. **[09-30 09:36]** [PATCH v3 2/9] KVM: selftests: Provide executables path option to the
 KVM selftest runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
4. **[09-30 09:36]** [PATCH v3 3/9] KVM: selftests: Add timeout option in selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
5. **[09-30 09:36]** [PATCH v3 4/9] KVM: selftests: Add option to save selftest runner
 output to a directory
   - 发件人: Vipin Sharma <vipinsh@google.com>
6. **[09-30 09:36]** [PATCH v3 5/9] KVM: selftests: Run tests concurrently in KVM
 selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
7. **[09-30 09:36]** [PATCH v3 6/9] KVM: selftests: Add various print flags to KVM
 selftest runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
8. **[09-30 09:36]** [PATCH v3 7/9] KVM: selftests: Print sticky KVM selftests runner
 status at bottom
   - 发件人: Vipin Sharma <vipinsh@google.com>
9. **[09-30 09:36]** [PATCH v3 8/9] KVM: selftests: Add rule to generate default tests for
 KVM selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
10. **[09-30 09:36]** [PATCH v3 9/9] KVM: selftests: Provide README.rst for KVM selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
11. **[09-30 15:23]** Re: [PATCH v3 1/9] KVM: selftest: Create KVM selftest runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
12. **[10-01 09:44]** Re: [PATCH v3 9/9] KVM: selftests: Provide README.rst for KVM selftests runner
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[10-01 10:32]** Re: [PATCH v3 9/9] KVM: selftests: Provide README.rst for KVM
 selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
14. **[10-02 15:41]** Re: [PATCH v3 9/9] KVM: selftests: Provide README.rst for KVM selftests runner
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[10-02 18:02]** Re: [PATCH v3 9/9] KVM: selftests: Provide README.rst for KVM
 selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[10-02 23:39]** Re: [PATCH v3 9/9] KVM: selftests: Provide README.rst for KVM
 selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>

---

### Thread 6: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 16 Sep 2025 13:27:39 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下如何将 MMIO（内存映射输入输出）捐赠给虚拟机监控器的补丁（PATCH v4 02/28）。

**原始补丁内容**：该补丁旨在改善 KVM 的 MMIO 处理，通过将 MMIO 捐赠给 hypervisor，以提高系统的性能和稳定性。

**历史讨论要点**：在之前的讨论中，参与者探讨了 MMIO 页的解除映射过程及其错误处理，认为在特定情况下，使用 WARN_ON 来处理错误是足够的。同时，Mostafa Saleh 提出在补丁中添加必要的检查，以避免调用者忘记处理错误。

**本周新讨论进展**：本周的讨论主要集中在补丁的进一步完善上。Mostafa 表示将为 v5 版本添加新的 MMIO 辅助函数，以处理错误路径。Jason Gunthorpe 提出了关于驱动程序核心的建议，认为在 KVM 初始化过程中，确保电源域在 SMMU（共享内存管理单元）之前被探测是有益的。此外，讨论还涉及 DMA API 如何正确使用 IOMMU_MMIO，以确保系统的稳定性和性能。

总体而言，讨论围绕如何优化 KVM 的 MMIO 处理和驱动程序加载顺序展开，参与者达成了一些共识，并计划在后续版本中进行改进。

#### 📝 邮件列表

1. **[09-16 13:27]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[09-16 14:24]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[09-23 14:35]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[09-23 14:38]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
5. **[09-26 15:33]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Will Deacon <will@kernel.org>
6. **[09-26 15:42]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Will Deacon <will@kernel.org>
7. **[09-29 10:57]** Re: [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[09-29 11:01]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[09-29 11:10]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[09-30 09:38]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
11. **[09-30 12:55]** Re: [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page
 table
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[10-02 12:13]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 7: [PATCH v7 03/12] mm: introduce AS_NO_DIRECT_MAP

**📧 邮件数**: 12 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 24 Sep 2025 16:10:43 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH v7 03/12] mm: introduce AS_NO_DIRECT_MAP”，主要讨论了在内存映射中引入 AS_NO_DIRECT_MAP 的提案。该补丁旨在为直接映射条目未设置的映射类型（如 secretmem 映射）提供支持，并计划在未来的 guest_memfd 配置中使用。

在历史讨论中，参与者们探讨了该补丁的必要性及其潜在影响。Patrick Roy 提到，当前的映射类型在某些情况下会被拒绝，主要是因为无法处理 secretmem 映射。其他参与者则对是否在直接映射操作后禁用 TLB 刷新进行了深入讨论，认为这可能会导致性能问题，尤其是在处理大量页面故障时。

在本周的新讨论中，David Hildenbrand 提出了一种可能的优化方案，即在访问某个地址时，先分配并准备同一块内存中的所有页面，然后只在调整完所有直接映射条目后再进行一次 TLB 刷新。讨论中还提到了一些架构能够无中断地刷新远程 TLB 的能力，以及关于异步 TLB 刷新的研究，认为这种方法可能在某些情况下比不进行显式 TLB 刷新更有效。

总体而言，本周的讨论集中在优化 TLB 刷新机制及其对性能的影响上，参与者们对如何平衡安全性与性能提出了不同的看法。

#### 📝 邮件列表

1. **[09-24 16:10]** [PATCH v7 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Patrick Roy <patrick.roy@campus.lmu.de>
2. **[09-24 15:22]** [PATCH v7 04/12] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
3. **[09-24 15:22]** [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling TLB
 flushing
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
4. **[09-25 11:27]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Dave Hansen <dave.hansen@intel.com>
5. **[09-25 21:20]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
6. **[09-25 12:59]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Dave Hansen <dave.hansen@intel.com>
7. **[09-25 22:13]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
8. **[09-26 10:46]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Patrick Roy <patrick.roy@linux.dev>
9. **[09-26 11:53]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for
 disabling TLB flushing
   - 发件人: Will Deacon <will@kernel.org>
10. **[09-26 22:09]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>
11. **[09-27 08:38]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Patrick Roy <patrick.roy@linux.dev>
12. **[09-29 12:20]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: David Hildenbrand <david@redhat.com>

---

### Thread 8: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 19 Sep 2025 16:50:56 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的内存过渡检查，特别是针对 pKVM 的内存范围参数的验证。原始的补丁（PATCH v2）由 Vincent Donnefort 提出，目的是在 pKVM 内存过渡中增加对主机发出的范围参数的检查，以防止潜在的溢出问题。

在历史讨论中，参与者们关注了补丁的边界检查逻辑，Marc Zyngier 提出了对范围结束边界的包含性检查的担忧，认为目前的实现可能导致合法范围被错误地判定为无效。Oliver Upton 也表达了对范围检查假设的担忧，认为应尽量减少对地址空间的假设。

在本周的新讨论中，Marc Zyngier 提出了一个新的检查函数的实现建议，旨在更好地处理边界问题。然而，Vincent Donnefort 对此表示担忧，指出仍然可能存在溢出的问题，特别是在某些情况下可能绕过其他检查函数，导致不安全的内存映射。

总体来看，讨论集中在如何确保内存范围检查的安全性和有效性，以防止潜在的安全漏洞。

#### 📝 邮件列表

1. **[09-19 16:50]** [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[09-21 12:29]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-22 22:00]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[09-22 16:33]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-23 10:18]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[10-01 10:37]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[10-03 14:45]** Re: [PATCH v2] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 9: [STABLE 5.15.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD register saving sequence

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  3 Oct 2025 19:39:17 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 FPSIMD（Floating Point SIMD）寄存器保存序列中的软中断屏蔽问题。

**原始补丁内容**：
补丁的目的是解决由于错误回溯导致的内核 BUG，确保在保存 FPSIMD/SVE/SME 状态时禁用和启用软中断。原补丁（提交 ID: 23249dade24e）修复了一个因错误回溯引起的内核崩溃问题。

**之前讨论要点**：
在历史讨论中，未提及具体的讨论内容，但可以推测该补丁的必要性是由于之前的实现存在问题，导致系统在处理软中断时可能出现死锁。

**本周的新讨论和进展**：
本周的讨论中，Will Deacon 提出了一个新的补丁，进一步改进了原始补丁，增加了在保存 FPSIMD 寄存器时禁用硬中断的措施，以防止在重新启用软中断时发生死锁。Ard Biesheuvel 对该补丁表示认可并确认了其有效性。邮件中还提到了一些技术细节和代码修改，确保系统在处理寄存器状态时的稳定性。

总的来说，本周的讨论集中在对补丁的改进和确认上，旨在进一步提升 KVM 在 arm64 架构下的稳定性和性能。

#### 📝 邮件列表

1. **[10-03 19:39]** [STABLE 5.15.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD register saving sequence
   - 发件人: Will Deacon <will@kernel.org>
2. **[10-03 19:43]** Re: [STABLE 5.15.y] [PATCH] KVM: arm64: Fix softirq masking in
 FPSIMD register saving sequence
   - 发件人: Will Deacon <will@kernel.org>
3. **[10-05 16:56]** Re: [STABLE 5.15.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD
 register saving sequence
   - 发件人: Ard Biesheuvel <ardb@kernel.org>

---

### Thread 10: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 26 Sep 2025 12:42:50 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 x86 架构下处理 PMU（性能监控单元）相关的补丁，具体是禁用对某些 PMU MSRs（模型特定寄存器）的拦截，以支持中介虚拟 PMU。

在历史讨论中，Sean Christopherson 提到在 AMD 处理器的某些情况下，尽管来宾缺少全局 MSRs，但仍然可以使用与主机能力一致的计数器数量，因此并不总是需要对 RDPMC（读取性能监控计数器）进行拦截。

在本周的新讨论中，Sean Christopherson 进一步探讨了 Intel 处理器的情况，并确认补丁的逻辑是正确的。他对补丁的代码修改表示认可，认为其实现良好。Sandipan Das 也对此表示感谢，确认了补丁的有效性。

总结来说，补丁旨在优化 KVM 对 PMU 的处理，历史讨论提供了背景信息，而本周的讨论则确认了补丁的合理性和有效性。

#### 📝 邮件列表

1. **[09-26 12:42]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sandipan Das <sandidas@amd.com>
2. **[10-01 11:14]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-03 10:33]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sandipan Das <sandidas@amd.com>

---

### Thread 11: [PATCH] KVM: arm64: Remove unreachable break after return

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 30 Sep 2025 16:56:21 +0300

#### 🤖 AI 总结

本邮件线程讨论的主题是一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要内容是移除在 `arch/arm64/kvm/at.c` 文件中一个位于 `return` 语句后的无效 `break` 语句。该补丁由 Osama Abdelkader 提出，目的是清理代码，提升可读性。

在之前的讨论中，并没有相关的历史邮件记录，因此本周的讨论是该补丁的主要内容。Osama Abdelkader 提交了补丁后，Zenghui Yu 对其进行了审核并表示支持，确认了补丁的有效性。随后，Marc Zyngier 也确认已将该补丁应用到修复列表中，并表示感谢。

综上所述，本周的讨论集中在补丁的提交、审核和应用上，标志着该代码改进的顺利推进。

#### 📝 邮件列表

1. **[09-30 16:56]** [PATCH] KVM: arm64: Remove unreachable break after return
   - 发件人: Osama Abdelkader <osama.abdelkader@gmail.com>
2. **[10-01 01:58]** Re: [PATCH] KVM: arm64: Remove unreachable break after return
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
3. **[10-01 09:55]** Re: [PATCH] KVM: arm64: Remove unreachable break after return
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH] KVM: selftests: fix irqfd_test on arm64

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 30 Sep 2025 08:14:19 -0700

#### 🤖 AI 总结

本邮件讨论的主题是修复 KVM 自测中的 `irqfd_test` 在 arm64 架构上的问题。原始的补丁（patch）由 Oliver Upton 提出，目的是解决在没有内核 IRQ 芯片的情况下，`KVM_IRQFD` ioctl 调用失败的问题。补丁通过添加一个架构谓词来判断默认虚拟机是否具有 IRQ 芯片，并调整 `irqfd_test` 的依赖关系，以适应不同架构的需求。

在之前的讨论中，Sean Christopherson 提到该问题正在影响开发者的持续集成（CI）环境，因此希望尽快推出修复，即使该修复不是最终版本。

在本周的新讨论中，Oliver 提到他在进行自测推广到 VHE EL2 时遇到的困难，并表示相关的修改已被纳入 Paolo 的代码库。此外，Sean 对补丁表示认可，并确认了其他参与者的报告。最终，Sean 给予了补丁的确认（Ack），表明他支持该修复的合并。

总的来说，本周的讨论集中在补丁的确认和对修复的认可上，强调了该问题的紧迫性和重要性。

#### 📝 邮件列表

1. **[09-30 08:14]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[09-30 11:26]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-30 12:29]** Re: [PATCH] KVM: selftests: fix irqfd_test on arm64
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 13: [PATCH] KVM: arm64: Prevent access to vCPU events before init

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 30 Sep 2025 01:52:37 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在防止在虚拟 CPU（vCPU）初始化之前访问 vCPU 事件。补丁的主要内容是拒绝在未初始化的 vCPU 上调用 ioctl 操作，以避免 KVM 处理未初始化状态导致的错误。

在历史讨论中，补丁的提出是由于 syzkaller 工具发现了一个 bug，具体表现为 KVM 允许用户空间在未初始化的 vCPU 上挂起事件，导致 KVM 解析错误的状态，进而引发内核错误（BUG）。该问题在 6.17 版本及以上的内核中尤为明显。

在本周的新讨论中，参与者 Oliver Upton 提出了补丁，并详细描述了问题的根源及其解决方案。Marc Zyngier 对补丁表示认可，并指出需要对返回的 -ENOEXEC 错误进行文档说明。最终，Marc 确认已将该补丁应用于修复分支，解决了这个令人烦恼的 bug。补丁的提交记录为 cc96679f3c0348bf8450a5c84b71bb1351c027f9。

#### 📝 邮件列表

1. **[09-30 01:52]** [PATCH] KVM: arm64: Prevent access to vCPU events before init
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-30 10:26]** Re: [PATCH] KVM: arm64: Prevent access to vCPU events before init
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-30 10:28]** Re: [PATCH] KVM: arm64: Prevent access to vCPU events before init
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [STABLE 6.1.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD register saving sequence

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  3 Oct 2025 19:40:18 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁，主要解决了在 FPSIMD（Floating Point SIMD）寄存器保存序列中软中断（softirq）屏蔽的问题。

**原始补丁内容**：
补丁的目标是修复因错误回溯导致的内核 BUG。之前的提交（8f4dc4e54eed）确保在保存 FPSIMD/SVE/SME 状态时禁用和启用软中断，但该修复可能导致死锁，因为重新启用软中断时可能会在持有锁的情况下处理待处理的软中断。

**之前的讨论要点**：
在历史讨论中，未提及具体的讨论内容，但可以推测补丁的初衷是解决内核中的严重错误，确保系统稳定性。

**本周的新讨论与进展**：
本周的讨论中，Will Deacon 提出了进一步的修复措施，建议在保存 FPSIMD 寄存器时同时禁用硬中断（hardirq），以防止死锁的发生。Ard Biesheuvel 对此补丁表示认可（Acked-by），表明该修复得到了支持并可能会被合并到主线代码中。

总结而言，本周的讨论集中在如何进一步改进补丁以避免潜在的死锁问题，确保 KVM 在 arm64 架构下的稳定性。

#### 📝 邮件列表

1. **[10-03 19:40]** [STABLE 6.1.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD register saving sequence
   - 发件人: Will Deacon <will@kernel.org>
2. **[10-05 16:56]** Re: [STABLE 6.1.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD
 register saving sequence
   - 发件人: Ard Biesheuvel <ardb@kernel.org>

---

### Thread 15: [STABLE 6.6.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD register saving sequence

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  3 Oct 2025 19:40:54 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 FPSIMD（Floating Point SIMD）寄存器保存序列中的软中断屏蔽问题。原始的补丁（patch）旨在解决因错误回溯导致的内核 BUG，确保在 FPSIMD 寄存器保存操作期间正确禁用和启用软中断。

在之前的讨论中，补丁 28b82be094e2 解决了一个由错误回溯引起的内核问题，但引入了新的死锁风险，因为在重新启用软中断时可能会导致在持有锁的情况下处理待处理的软中断。这引发了对如何进一步改进的讨论。

在本周的新讨论中，Will Deacon 提出了一个改进方案，通过在保存 FPSIMD 寄存器时禁用硬中断来减少死锁的风险，并更新了相关代码。Ard Biesheuvel 对该补丁表示认可（Acked-by），表明该修改得到了支持和认可。

总的来说，本周的讨论集中在如何在修复原有问题的同时，避免引入新的死锁问题，并且得到了参与者的积极反馈。

#### 📝 邮件列表

1. **[10-03 19:40]** [STABLE 6.6.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD register saving sequence
   - 发件人: Will Deacon <will@kernel.org>
2. **[10-05 16:56]** Re: [STABLE 6.6.y] [PATCH] KVM: arm64: Fix softirq masking in FPSIMD
 register saving sequence
   - 发件人: Ard Biesheuvel <ardb@kernel.org>

---

### Thread 16: [PATCH] KVM: arm64: nv: do not inject L2-bound IRQs to L1 hypervisor

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 2 Oct 2025 21:00:11 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在解决 L1 虚拟机监控程序（hypervisor）处理 L2 绑定中断（IRQ）时出现的问题。

**原始补丁内容**：
补丁的核心是防止将 L2 绑定的中断注入到 L1 虚拟机监控程序中。当前的实现中，KVM 在处理虚拟中断时，未能正确管理中断列表（LRs），导致在 L1 虚拟机监控程序尝试处理新中断时可能出现错误，尤其是在活跃中断数量达到 LRs 限制时。

**之前讨论要点**：
在历史讨论中，未提及具体的补丁内容，但可以推测之前的讨论集中在 KVM 如何处理虚拟中断及其对嵌套虚拟化的影响。补丁的提出是为了修复在非嵌套情况下正常的中断处理在嵌套情况下出现的问题。

**本周的新讨论与进展**：
本周的讨论中，补丁的提出者 Volodymyr Babchuk 详细阐述了问题的根源及补丁的解决方案，强调了 L1 虚拟机监控程序在处理中断时的行为。Oliver Upton 对补丁提出了质疑，指出当前的解决方案可能会违反 GIC 的架构模型，并建议调整中断排序，以确保待处理的中断优先填充 LRs。这表明对补丁的讨论仍在继续，且存在不同的解决方案建议。

#### 📝 邮件列表

1. **[10-02 21:00]** [PATCH] KVM: arm64: nv: do not inject L2-bound IRQs to L1 hypervisor
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
2. **[10-02 17:04]** Re: [PATCH] KVM: arm64: nv: do not inject L2-bound IRQs to L1
 hypervisor
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 17: [PATCH] KVM: selftests: Fix irqfd_test for non-x86 architectures

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 30 Sep 2025 12:33:02 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 自测试中的 irqfd_test，以支持非 x86 架构。原始的 patch 由 Oliver Upton 提出，主要问题在于 KVM_IRQFD ioctl 在内核中没有 irqchip 时会失败，这在非 x86 架构上尤为明显。之前的测试假设默认虚拟机会隐式创建一个内核中的 irqchip，但这并不适用于所有架构。

在本周的新讨论中，Oliver Upton 提出了具体的修复方案，增加了一个架构谓词来判断默认虚拟机是否会获得 irqchip，并使 irqfd_test 依赖于此。为了解决 arm64 架构的 VGIC 初始化要求，使用了 vm_create_with_one_vcpu() 函数，并忽略了创建的 vCPU，因为在测试中并未使用到。

Marc Zyngier 在随后的邮件中确认了该 patch 的应用，并表示感谢。最终，该 patch 被成功合并，解决了非 x86 架构下的测试问题。

#### 📝 邮件列表

1. **[09-30 12:33]** [PATCH] KVM: selftests: Fix irqfd_test for non-x86 architectures
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[10-01 09:55]** Re: [PATCH] KVM: selftests: Fix irqfd_test for non-x86 architectures
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH v2] KVM: arm64: Document vCPU event ioctls as requiring init'ed vCPU

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 30 Sep 2025 16:36:20 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vCPU 事件 ioctl 的文档更新。原始的 patch（补丁）由 Oliver Upton 提出，目的是更新 API 文档，以明确指出对未初始化的 vCPU 调用 KVM_{GET,SET}_VCPU_EVENTS 会被拒绝，并返回错误代码 -ENOEXEC。这一变化是基于之前的提交（commit cc96679f3c03），该提交防止在 vCPU 初始化之前访问 vCPU 事件。

在之前的讨论中，主要集中在确保文档的准确性和清晰性，以帮助开发者理解在使用这些 ioctl 时的要求。

在本周的新讨论中，Oliver Upton 提交了补丁的 v2 版本，增加了相关文档的说明，并在文档中明确指出对未初始化 vCPU 的 ioctl 调用会返回 -ENOEXEC。随后，Marc Zyngier 回复确认已将该补丁应用于修复分支，并表示感谢。这表明补丁得到了认可并已被合并。

#### 📝 邮件列表

1. **[09-30 16:36]** [PATCH v2] KVM: arm64: Document vCPU event ioctls as requiring init'ed vCPU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[10-01 09:29]** Re: [PATCH v2] KVM: arm64: Document vCPU event ioctls as requiring init'ed vCPU
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH 3/6] KVM: arm64: Add pre_fault_memory implementation

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 29 Sep 2025 14:59:35 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下实现 `pre_fault_memory` 的补丁（patch）。该补丁的目的是在处理内存访问故障时，提供更好的错误处理机制。

在历史讨论中，未提及具体的背景信息，但本周的讨论集中在补丁的实现细节上。参与者 Jack Thomson 和 Oliver Upton 对补丁的代码进行了审查和讨论。Jack 提到，补丁的实现看起来更好，尤其是引入了合成中止（synthetic abort）的处理方式。Oliver 则建议对整个结构体进行快照，以便于未来兼容新字段的添加，并指出在处理访问标志故障时，应该更准确地表示为翻译故障，而不是在 `user_mem_abort()` 中处理。

此外，Oliver 还提到补丁中缺少一些与错误状态寄存器（ESR）相关的重要字段，这些字段对于正确指示数据中止至关重要。他建议在补丁中进行相应的修改，以确保更准确的故障处理。

总的来说，本周的讨论主要集中在补丁的代码细节和改进建议上，参与者们积极交流，推动补丁的完善。

#### 📝 邮件列表

1. **[09-29 14:59]** Re: [PATCH 3/6] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
2. **[09-29 17:53]** Re: [PATCH 3/6] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 3 Oct 2025 14:34:23 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA”的补丁系列。该补丁旨在通过 KVM_EXIT_ARM_SEA 机制，使虚拟机监控程序（VMM）能够处理来自虚拟机的 SEA（System Error Acknowledge）信号。这一功能的实现将增强 KVM 对 ARM 架构虚拟机的支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了改善虚拟化环境中对 ARM 架构的错误处理能力，可能涉及到对现有 KVM 处理机制的改进。

在本周的新讨论中，参与者 Jiaqi Yan 向邮件列表中的其他成员请求对该补丁系列的审查，并表示非常欢迎任何评论和反馈。他还提到之前的邮件因格式问题被重新发送。这表明该补丁系列仍在积极寻求社区的意见，以便进行进一步的修改和完善。

总体来看，本周的讨论主要集中在对补丁的审查请求上，尚未有具体的技术反馈或进展更新。

#### 📝 邮件列表

1. **[10-03 14:34]** Re: [PATCH v3 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 21: [PATCH 15/34] KVM: Add KVM_CREATE_GUEST_MEMFD ioctl() for
 guest-specific backing memory

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 3 Oct 2025 18:23:57 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中的一个补丁，具体是添加 `KVM_CREATE_GUEST_MEMFD ioctl()` 用于支持特定于虚拟机的后备内存。

在历史讨论中，补丁的主要目的是为虚拟机提供一个新的接口，以便更灵活地管理其内存，特别是在需要进行快照或迁移时。

本周的讨论中，参与者 Nikita Kalyazin 提出了一个问题，询问在当前阶段是否仍然需要对某些限制进行保留，特别是在虚拟机内存可以被主机访问的情况下。他指出，这种限制的解除将有助于支持基于脏页跟踪的差异快照功能，尤其是在 Firecracker 中进行快照或实时迁移时。Nikita 进行了实验，去掉了相关检查，成功生成了差异快照并从中恢复了 Firecracker 虚拟机，显示出这一改动的潜在价值。

总结而言，本周的讨论集中在对补丁的限制进行审视，以及如何通过实验验证其在实际应用中的可行性。

#### 📝 邮件列表

1. **[10-03 18:23]** Re: [PATCH 15/34] KVM: Add KVM_CREATE_GUEST_MEMFD ioctl() for
 guest-specific backing memory
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>

---

### Thread 22: [PATCH] KVM: arm64: nv: do not inject L2-bound IRQs to L1
 hypervisor

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 3 Oct 2025 13:48:38 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在防止将 L2 绑定的中断注入到 L1 虚拟机监控器（hypervisor）中。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了优化中断处理，确保 L1 虚拟机监控器不会受到 L2 中断的干扰，从而提高虚拟化性能和稳定性。

在本周的新讨论中，参与者 Volodymyr Babchuk 对补丁的背景表示了理解，并提到他之前未能注意到相关特性（LRENPIE 位）。他表示由于工作优先级的变化，无法继续投入更多精力到该问题上，并希望其他人能接手此项工作。此外，他提到无法提供重现该问题的具体示例，因为这需要复杂的 Android 构建环境，但他怀疑该问题可以通过在 kvmtool 中同时触发大量中断来重现，并指出这与 Xen 无关，KVM 作为 L1 虚拟机监控器也应能正常工作。

总体来看，讨论显示出对补丁的认可，但也反映出参与者在时间和资源上的限制，导致后续工作可能需要其他开发者的支持。

#### 📝 邮件列表

1. **[10-03 13:48]** Re: [PATCH] KVM: arm64: nv: do not inject L2-bound IRQs to L1
 hypervisor
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>

---

### Thread 23: [PATCH] KVM: arm64: Document vCPU event ioctls as requiring init'ed vCPU

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 30 Sep 2025 15:15:21 -0700

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: Document vCPU event ioctls as requiring init'ed vCPU”，由 Oliver Upton 提交。该补丁的主要内容是更新 KVM 的 API 文档，明确指出在未初始化的虚拟 CPU（vCPU）上调用 KVM_{GET,SET}_VCPU_EVENTS 将会被拒绝，并返回错误代码 -ENXIO。这一变更是基于之前的提交（commit cc96679f3c03），该提交的目的是防止在 vCPU 初始化之前访问 vCPU 事件。

在历史讨论中并没有相关的内容，因此本次讨论主要集中在补丁的具体实现和文档更新上。Oliver Upton 在补丁中增加了三行文档，清晰地说明了在未初始化的 vCPU 上调用相关 ioctl 的后果。

本周的新讨论仅限于这一补丁的提交，没有其他参与者的回复或进一步的讨论。整体来看，此补丁旨在提高 KVM 的 API 文档的准确性和可用性，确保开发者在使用相关功能时能够清楚地理解其前提条件。

#### 📝 邮件列表

1. **[09-30 15:15]** [PATCH] KVM: arm64: Document vCPU event ioctls as requiring init'ed vCPU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

## 📌 Selftest

共 1 个 thread

---

### Thread 1: selftests: kvm: irqfd_test: KVM_IRQFD failed, rc: -1 errno: 11
 (Resource temporarily unavailable)

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 30 Sep 2025 16:29:54 +0530

#### 🤖 AI 总结

本邮件线程讨论了 KVM 的自测试 irqfd_test 在多个平台上持续失败的问题。Naresh Kamboju 提到，自从 Linux next-20250625 引入该测试以来，所有测试平台上均出现 KVM_IRQFD ioctl 返回 errno 11（资源暂时不可用）的情况，且这一问题在所有测试运行中均可重现，失败率达到 100%。具体失败的平台包括 graviton4 和 rk3399-rock-pi-4b。

在本周的讨论中，Sean Christopherson 指出这是一个已知问题，主要原因在于 KVM ARM 需要测试创建一个虚拟通用中断控制器（vGIC），但修复工作进展缓慢，因为没有一个明显正确的解决方案。Sean 还提到将会联系其他相关人员以推动问题的解决。

总结来看，当前的主要问题是 irqfd_test 在 ARM 平台上因资源不足而失败，需进一步探讨是否将其视为不支持的情况，或是需要补充实现和配置。

#### 📝 邮件列表

1. **[09-30 16:29]** selftests: kvm: irqfd_test: KVM_IRQFD failed, rc: -1 errno: 11
 (Resource temporarily unavailable)
   - 发件人: Naresh Kamboju <naresh.kamboju@linaro.org>
2. **[09-30 08:11]** Re: selftests: kvm: irqfd_test: KVM_IRQFD failed, rc: -1 errno: 11
 (Resource temporarily unavailable)
   - 发件人: Sean Christopherson <seanjc@google.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 updates for 6.18

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 25 Sep 2025 19:26:11 +0100

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.18 版本中的更新，主要由 Marc Zyngier 提出并由 Paolo Bonzini 回复。

**原始 patch/问题的内容**：
Marc Zyngier 提交了一系列针对 KVM/arm64 的更新，主要包括修复一些问题和解决架构上的缺陷。其中，值得注意的是新增了一个基本框架，以便在 EL2 层以较为透明的方式运行 EL1 测试。此外，pKVM 方面唯一的新内容是 FF-A 1.2 的支持。

**之前讨论要点**：
在历史讨论中，Marc 提到这些更新包含了许多修复和改进，具体细节在邮件中有附加说明。他还以讽刺的口吻提到 FF-A 1.2 的支持可能不会对世界产生重大影响。

**本周的新讨论、进展或结论**：
在本周的讨论中，Paolo Bonzini 对 Marc 的更新表示认可，并感谢其提交，表示已经将这些更新合并，并对延迟表示歉意。整体来看，本周的讨论主要是对之前更新的确认和感谢，没有提出新的问题或建议。

#### 📝 邮件列表

1. **[09-25 19:26]** [GIT PULL] KVM/arm64 updates for 6.18
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-30 19:12]** Re: [GIT PULL] KVM/arm64 updates for 6.18
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 3 个 thread

---

### Thread 1: KVM: Nested VGIC emulation leads to infinite IRQ exceptions

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 2 Oct 2025 12:29:42 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 中嵌套 VGIC 模拟导致无限 IRQ 异常的问题。

1. **原始问题**：该问题涉及 KVM 的嵌套 VGIC 模拟，具体表现为在处理 IRQ 时出现无限循环的异常，影响系统的正常运行。

2. **之前讨论要点**：在历史讨论中，参与者们探讨了问题的复杂性，特别是与 Android 构建环境的关联，导致难以共享重现该问题的设置。同时，讨论中提到需要对 QEMU 进行补丁以启用某些功能。

3. **本周的新讨论与进展**：本周，Volodymyr Babchuk 提供了更多的调试信息，指出在处理 IRQ 时，存在多个活动中断填满了可用的 LR（中断路由），导致无法正确处理定时器中断。他提出了两种可能的解决方案：优先处理定时器中断或降低活动中断的优先级。Marc Zyngier 则对中断处理的逻辑提出了质疑，认为 DomU 的中断不应影响 Xen，并指出 KVM 中缺少某些功能，可能是导致问题的原因，但尚未明确解决方案。

总体来看，本周的讨论集中在问题的根源分析及可能的解决方案上，尚需进一步的探讨与验证。

#### 📝 邮件列表

1. **[10-02 12:29]** Re: KVM: Nested VGIC emulation leads to infinite IRQ exceptions
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>
2. **[10-02 15:28]** Re: KVM: Nested VGIC emulation leads to infinite IRQ exceptions
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: KVM: Nested VGIC emulation leads to infinite IRQ exceptions

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 01 Oct 2025 08:23:09 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 中嵌套 VGIC 模拟导致无限 IRQ 异常的问题。邮件中并没有提供历史讨论的内容，主要集中在本周的讨论。

本周的讨论中，Marc Zyngier 针对 Volodymyr Babchuk 提出的情况进行了深入分析。他指出，当前使用的 9.2 版本缺乏 NV 支持，建议使用 10.1 版本，并询问了在读取 IAR 时 Xen 中 ICH_HCR_EL2 的配置情况。他的推测是，可能在处理维护中断时禁用了虚拟 CPU 接口，导致无法确认中断。

随后，Marc 进一步分析了问题，指出 EL2 的物理定时器和 EL1 的虚拟定时器都处于待处理状态，暗示可能存在 KVM 或 Xen 中的某种问题。他建议进行更多的调试，以便更好地理解当前的中断处理情况。

总的来说，本周的讨论围绕如何解决嵌套 VGIC 模拟中的 IRQ 异常展开，Marc 提出了多项调试建议，但仍需更多信息以便进一步分析。

#### 📝 邮件列表

1. **[10-01 08:23]** Re: KVM: Nested VGIC emulation leads to infinite IRQ exceptions
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-01 17:17]** Re: KVM: Nested VGIC emulation leads to infinite IRQ exceptions
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: KVM: Nested VGIC emulation leads to infinite IRQ exceptions

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 2 Oct 2025 15:08:09 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中嵌套 VGIC（虚拟通用中断控制器）仿真导致的无限 IRQ 异常问题。

在本周的讨论中，参与者 Volodymyr Babchuk 针对 Marc Zyngier 提出的观点进行了回应，讨论了 KVM 在处理 IRQ 时的行为。他指出，当前的 IRQ 处理机制似乎没有正确跟踪被重新注入的 IRQ，导致这些 IRQ 仍然保留在 Xen 的中断路由中。他认为，KVM 应该能够识别并移除这些重新注入的 IRQ，以避免无限异常的发生。

同时，Babchuk 提出了一个可能的解决方案，即通过检查 vLR（虚拟链接寄存器）中的硬件位来区分 L1（第一层）和 L2（第二层）虚拟机的 IRQ。这种方法依赖于 L1 虚拟化层的良好行为，即它不会试图关闭已经注入到其客体中的 IRQ。他承认，这在处理由真实硬件设备生成的中断时可能会变得复杂。

总的来说，本周的讨论集中在如何改进 KVM 的 IRQ 处理机制，以解决嵌套虚拟化环境中出现的无限 IRQ 异常问题，并提出了一些初步的解决思路。

#### 📝 邮件列表

1. **[10-02 15:08]** Re: KVM: Nested VGIC emulation leads to infinite IRQ exceptions
   - 发件人: Volodymyr Babchuk <Volodymyr_Babchuk@epam.com>

---

