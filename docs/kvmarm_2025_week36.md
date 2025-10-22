# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:48:38

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 200
- **总 Thread 数**: 33
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 31 threads (196 邮件)
- **Other**: 2 threads (4 邮件)

---

## 📌 PATCH

共 31 个 thread

---

### Thread 1: [PATCH v8 00/29] KVM: arm64: Implement support for SME

**📧 邮件数**: 30 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 02 Sep 2025 12:36:03 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构上实现对 SME（Scalable Matrix Extension）的支持，包含多个补丁的提交和讨论。

1. **原始补丁内容**：补丁系列的核心是实现对 SME 的支持，允许 KVM 虚拟机使用 SME 特性。SME 引入了新的向量长度和控制寄存器，类似于 SVE（Scalable Vector Extension），但有其独特的寄存器和状态管理。

2. **历史讨论要点**：之前的讨论主要集中在如何设计用户空间 ABI、寄存器访问的控制，以及如何处理 SME 和 SVE 的最终化过程。补丁中提到，SME 和 SVE 的最终化将通过一个共同的接口进行，以避免复杂性。

3. **本周的新讨论和进展**：
   - 本周的讨论中，Mark Brown 移除了 RFC 标签，表示补丁已准备好进行审查。补丁中详细说明了 SME 的用户空间接口，特别是 ZA 和 ZT0 寄存器的访问。
   - 讨论了如何在 KVM 中处理 SME 特有的状态保存和恢复，包括在上下文切换时的状态管理。
   - 还增加了对 SME 异常的处理，确保在不支持 SME 的情况下，能够正确处理相关的异常。
   - 进一步的补丁更新了 KVM 的自测用例，以确保新引入的 SME 寄存器能够被正确识别和测试。

总的来说，本周的讨论和补丁提交标志着 KVM 对 SME 支持的逐步完善，涵盖了寄存器管理、状态保存与恢复及异常处理等多个方面。

#### 📝 邮件列表

1. **[09-02 12:36]** [PATCH v8 00/29] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-02 12:36]** [PATCH v8 01/29] arm64/sysreg: Update SMIDR_EL1 to DDI0601 2025-06
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[09-02 12:36]** [PATCH v8 02/29] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[09-02 12:36]** [PATCH v8 03/29] arm64/fpsimd: Decide to save ZT0 and streaming
 mode FFR at bind time
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[09-02 12:36]** [PATCH v8 04/29] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[09-02 12:36]** [PATCH v8 05/29] arm64/fpsimd: Determine maximum virtualisable SME
 vector length
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[09-02 12:36]** [PATCH v8 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[09-02 12:36]** [PATCH v8 07/29] KVM: arm64: Pay attention to FFR parameter in SVE
 save and load
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[09-02 12:36]** [PATCH v8 08/29] KVM: arm64: Pull ctxt_has_ helpers to start of
 sysreg-sr.h
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[09-02 12:36]** [PATCH v8 09/29] KVM: arm64: Move SVE state access macros after
 feature test macros
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[09-02 12:36]** [PATCH v8 10/29] KVM: arm64: Rename SVE finalization constants to
 be more general
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[09-02 12:36]** [PATCH v8 11/29] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[09-02 12:36]** [PATCH v8 12/29] KVM: arm64: Define internal features for SME
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[09-02 12:36]** [PATCH v8 13/29] KVM: arm64: Rename sve_state_reg_region
   - 发件人: Mark Brown <broonie@kernel.org>
15. **[09-02 12:36]** [PATCH v8 14/29] KVM: arm64: Store vector lengths in an array
   - 发件人: Mark Brown <broonie@kernel.org>
16. **[09-02 12:36]** [PATCH v8 15/29] KVM: arm64: Implement SME vector length
 configuration
   - 发件人: Mark Brown <broonie@kernel.org>
17. **[09-02 12:36]** [PATCH v8 16/29] KVM: arm64: Support SME control registers
   - 发件人: Mark Brown <broonie@kernel.org>
18. **[09-02 12:36]** [PATCH v8 17/29] KVM: arm64: Support TPIDR2_EL0
   - 发件人: Mark Brown <broonie@kernel.org>
19. **[09-02 12:36]** [PATCH v8 18/29] KVM: arm64: Support SME identification registers
 for guests
   - 发件人: Mark Brown <broonie@kernel.org>
20. **[09-02 12:36]** [PATCH v8 19/29] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>
21. **[09-02 12:36]** [PATCH v8 20/29] KVM: arm64: Provide assembly for SME register
 access
   - 发件人: Mark Brown <broonie@kernel.org>
22. **[09-02 12:36]** [PATCH v8 21/29] KVM: arm64: Support userspace access to streaming
 mode Z and P registers
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[09-02 12:36]** [PATCH v8 22/29] KVM: arm64: Flush register state on writes to
 SVCR.SM and SVCR.ZA
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[09-02 12:36]** [PATCH v8 23/29] KVM: arm64: Expose SME specific state to
 userspace
   - 发件人: Mark Brown <broonie@kernel.org>
25. **[09-02 12:36]** [PATCH v8 24/29] KVM: arm64: Context switch SME state for guests
   - 发件人: Mark Brown <broonie@kernel.org>
26. **[09-02 12:36]** [PATCH v8 25/29] KVM: arm64: Handle SME exceptions
   - 发件人: Mark Brown <broonie@kernel.org>
27. **[09-02 12:36]** [PATCH v8 26/29] KVM: arm64: Expose SME to nested guests
   - 发件人: Mark Brown <broonie@kernel.org>
28. **[09-02 12:36]** [PATCH v8 27/29] KVM: arm64: Provide interface for configuring and
 enabling SME for guests
   - 发件人: Mark Brown <broonie@kernel.org>
29. **[09-02 12:36]** [PATCH v8 28/29] KVM: arm64: selftests: Add SME system registers
 to get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
30. **[09-02 12:36]** [PATCH v8 29/29] KVM: arm64: selftests: Add SME to set_id_regs
 test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 2: [PATCH v5 02/12] arch: export set_direct_map_valid_noflush to KVM module

**📧 邮件数**: 23 | **👥 参与者**: 5 | **📅 开始时间**: Thu, 28 Aug 2025 11:07:11 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Linux 内核的补丁（PATCH v5 02/12），其内容是将 `set_direct_map_valid_noflush` 函数导出到 KVM 模块。补丁的目的是为了改善 KVM 的内存管理，确保在直接映射的上下文中可以有效地设置内存页的有效性。

在历史讨论中，参与者们对补丁的实现细节进行了审查，提出了一些建议和修正意见。例如，Fuad Tabba 指出补丁中的某些用法需要修正，并给予了“Reviewed-by”的标记。其他参与者也对补丁的描述和实现提出了警告和改进建议。

在本周的新讨论中，参与者们继续围绕补丁的细节展开讨论，Roy Patrick 对之前的反馈进行了回应，并确认了一些建议的实施。同时，关于函数参数的 `const` 修饰符的使用也引发了讨论，参与者们一致认为在函数定义中应保持一致性，以避免未来的调试困难。整体来看，本周的讨论主要集中在补丁的细节修正和代码一致性上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[08-28 11:07]** Re: [PATCH v5 02/12] arch: export set_direct_map_valid_noflush to KVM module
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[08-28 11:21]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[08-28 12:27]** Re: [PATCH v5 05/12] KVM: Documentation: describe
 GUEST_MEMFD_FLAG_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>
4. **[08-28 17:26]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Mike Rapoport <rppt@kernel.org>
5. **[08-28 17:54]** Re: [PATCH v5 04/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
6. **[08-28 23:00]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>
7. **[08-31 18:26]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: kernel test robot <lkp@intel.com>
8. **[09-01 13:47]** Re: [PATCH v5 02/12] arch: export set_direct_map_valid_noflush to KVM
 module
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
9. **[09-01 13:54]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
10. **[09-01 13:56]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
11. **[09-01 14:03]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
12. **[09-01 14:05]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
13. **[09-01 14:22]** Re: [PATCH v5 04/12] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
14. **[09-01 17:27]** Re: [PATCH v5 04/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
15. **[09-01 14:30]** Re: [PATCH v5 05/12] KVM: Documentation: describe
 GUEST_MEMFD_FLAG_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
16. **[09-01 16:43]** Re: [PATCH v5 05/12] KVM: Documentation: describe
 GUEST_MEMFD_FLAG_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>
17. **[09-01 14:56]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
18. **[09-02 08:59]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[09-02 10:46]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>
20. **[09-02 09:50]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Fuad Tabba <tabba@google.com>
21. **[09-02 09:18]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
22. **[09-02 10:21]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Fuad Tabba <tabba@google.com>
23. **[09-02 11:54]** Re: [PATCH v5 03/12] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: David Hildenbrand <david@redhat.com>

---

### Thread 3: [PATCH 0/5] KVM: arm64: GICv5 legacy (GCIE_LEGACY) NV enablement and
 cleanup

**📧 邮件数**: 19 | **👥 参与者**: 6 | **📅 开始时间**: Thu, 28 Aug 2025 10:59:41 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下对 GICv5 传统（GCIE_LEGACY）支持的启用及清理工作。历史讨论中，Sascha Bischoff 提出了一个补丁系列，旨在为基于 GICv3 的虚拟机在 GICv5 主机上启用嵌套虚拟化，并修复 ICC_SRE_EL2 访问处理，以符合更新的规范。此外，补丁还引入了一个 CPU 功能标志，用于跟踪所有 CPU 对 GCIE_LEGACY 的支持。

在本周的新讨论中，参与者对补丁进行了审查和确认。Suzuki K Poulose 和 Thomas Gleixner 对补丁的相关部分表示认可，并给予了“Reviewed-by”和“Acked-by”的反馈。Oliver Upton 提出了针对 VGIC（虚拟通用中断控制器）的一系列补丁，解决了锁定顺序问题，并改进了 LPI（本地外部中断）的引用计数管理，确保在释放 LPI 时不会引发竞态条件。此外，Oliver 还提出了不再需要在某些情况下禁用 IRQ 的建议，以简化锁定机制。

总体来看，本周的讨论集中在对补丁的审查、改进建议以及对潜在问题的修复上，推动了 GICv5 支持的进一步完善。

#### 📝 邮件列表

1. **[08-28 10:59]** [PATCH 0/5] KVM: arm64: GICv5 legacy (GCIE_LEGACY) NV enablement and
 cleanup
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[08-28 10:59]** [PATCH 3/5] arm64: cpucaps: Add GICv5 Legacy vCPU interface
 (GCIE_LEGACY) capability
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[08-28 10:59]** [PATCH 5/5] irqchip/gic-v5: Drop has_gcie_v3_compat from gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[09-02 09:23]** Re: [PATCH 3/5] arm64: cpucaps: Add GICv5 Legacy vCPU interface
 (GCIE_LEGACY) capability
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
5. **[09-03 14:07]** Re: [PATCH 5/5] irqchip/gic-v5: Drop has_gcie_v3_compat from
 gic_kvm_info
   - 发件人: Thomas Gleixner <tglx@linutronix.de>
6. **[09-03 23:23]** [PATCH 0/5] KVM: arm64: vgic-v3: Fix yet another lock ordering turd
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-03 23:23]** [PATCH 1/5] KVM: arm64: vgic-v3: Use bare refcount for VGIC LPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-03 23:23]** [PATCH 2/5] KVM: arm64: Spin off release helper from vgic_put_irq()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[09-03 23:23]** [PATCH 3/5] KVM: arm64: vgic-v3: Erase LPIs from xarray outside of raw spinlocks
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[09-03 23:23]** [PATCH 4/5] KVM: arm64: vgic-v3: Don't require IRQs be disabled for LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[09-03 23:23]** [PATCH 5/5] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may take LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[09-04 00:57]** Re: [PATCH 0/5] KVM: arm64: GICv5 legacy (GCIE_LEGACY) NV enablement
 and cleanup
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[09-04 01:19]** Re: [PATCH 5/5] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may
 take LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[09-04 11:25]** Re: [PATCH 5/5] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may take
 LPI xarray lock
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[09-05 00:19]** Re: [PATCH 3/5] KVM: arm64: vgic-v3: Erase LPIs from xarray outside
 of raw spinlocks
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[09-05 08:44]** Re: [PATCH 3/5] KVM: arm64: vgic-v3: Erase LPIs from xarray outside of raw spinlocks
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[09-05 09:13]** Re: [PATCH 4/5] KVM: arm64: vgic-v3: Don't require IRQs be disabled for LPI xarray lock
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[09-05 09:29]** Re: [PATCH 0/5] KVM: arm64: vgic-v3: Fix yet another lock ordering turd
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[09-05 01:55]** Re: [PATCH 4/5] KVM: arm64: vgic-v3: Don't require IRQs be disabled
 for LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 4: [PATCH v4 0/5] initialize SCTRL2_ELx

**📧 邮件数**: 16 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 21 Aug 2025 18:24:03 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于初始化 ARM 架构中的 SCTLR2_ELx 寄存器的补丁系列（[PATCH v4 0/5]）。该补丁旨在为 Linux 提供对 SCTLR2_ELx 寄存器的初步支持，这一特性在 ARMv8.8/ARMv9.3 版本中为可选，ARMv8.9/ARMv9.4 版本中为强制要求。尽管当前 Linux 不严格需要修改 SCTLR2_ELx，但未来的一些架构特性（如 FEAT_PAuth_LR 和 FEAT_CPA2）将需要配置这些寄存器的控制位。

在历史讨论中，Yeoreum Yun 提出了补丁的基本框架，强调了在 CPU 启动时初始化 SCTLR2_ELx 的必要性，以防止由于寄存器未正确初始化而导致的系统异常。

在本周的新讨论中，Dave Martin 对补丁提出了具体的技术建议，包括在汇编代码中增加错误检查和字符串比较，以确保寄存器的正确初始化顺序。他还询问了 SCTLR2_EL1 和 SCTLR_EL1 初始化的顺序是否有必要，并指出 SCTLR2_ELx 的初始化可能与 KVM 的寄存器管理有关。Yeoreum Yun 回应称他已测试了相关路径，并确认 SCTLR2_ELx 的值按预期设置。总体而言，讨论集中在补丁的细节和潜在的测试需求上，双方对补丁的方向表示认可，但仍需进一步验证和完善。

#### 📝 邮件列表

1. **[08-21 18:24]** [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[08-21 18:24]** [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[08-21 18:24]** [PATCH v4 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[09-01 11:08]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[09-01 16:13]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Dave Martin <Dave.Martin@arm.com>
6. **[09-01 16:13]** Re: [PATCH v4 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Dave Martin <Dave.Martin@arm.com>
7. **[09-01 16:18]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Dave Martin <Dave.Martin@arm.com>
8. **[09-01 19:17]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[09-01 19:29]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[09-01 19:33]** Re: [PATCH v4 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[09-02 11:39]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Dave Martin <Dave.Martin@arm.com>
12. **[09-02 12:05]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
13. **[09-03 11:43]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Dave Martin <Dave.Martin@arm.com>
14. **[09-03 11:52]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Dave Martin <Dave.Martin@arm.com>
15. **[09-03 11:59]** Re: [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
16. **[09-03 13:08]** Re: [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 5: [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 13 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 01 Sep 2025 13:40:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARMv8.8 SPE（Statistical Profiling Extension）特性的支持，主要涉及三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 FEAT_SPE_FDS 数据源过滤。James Clark 提出了一个包含 12 个补丁的系列，旨在实现这些特性。

在历史讨论中，补丁的版本经历了多次修改，主要集中在修复文档中的错误、重构代码以提高可读性和可维护性，以及解决与其他内核功能的冲突。补丁的主要内容包括对系统寄存器的更新、性能工具的修改以及文档的补充。

本周的新讨论中，James Clark 提交了多个补丁，具体进展如下：
1. **补丁 1**：增加了新的 PMSFCR_EL1 字段和 PMSDSFR_EL1 寄存器，以支持 FEAT_SPE_EFT 和 FEAT_SPE_FDS。
2. **补丁 2**：实现了 FEAT_SPEv1p4 过滤器的支持，改进了过滤器的可扩展性。
3. **补丁 3**：暴露了事件过滤器的能力，以便用户空间能够识别可过滤的事件。
4. **补丁 4**：增加了对 FEAT_SPE_EFT 的支持，允许更复杂的过滤条件。
5. **补丁 5**：实现了数据源过滤功能，允许基于数据源的过滤。
6. **补丁 6**：重构了检查 SPE 版本的宏，以提高代码可读性。
7. **补丁 7**：为 SPE_FEAT_FDS 启用 EL2 相关的要求。
8. **补丁 8**：为 PMSDSFR_EL1 添加了 KVM 的陷阱配置。
9. **补丁 9**：增加了新的 perf_event_attr::config4 字段，以支持数据源过滤。
10. **补丁 10**：实现了对数据源过滤的支持。
11. **补丁 11**：同步了用户空间头文件与内核源代码。
12. **补丁 12**：更新了文档，详细描述了新特

#### 📝 邮件列表

1. **[09-01 13:40]** [PATCH v8 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[09-01 13:40]** [PATCH v8 01/12] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: James Clark <james.clark@linaro.org>
3. **[09-01 13:40]** [PATCH v8 02/12] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[09-01 13:40]** [PATCH v8 03/12] perf: arm_spe: Expose event filter
   - 发件人: James Clark <james.clark@linaro.org>
5. **[09-01 13:40]** [PATCH v8 04/12] perf: arm_spe: Add support for FEAT_SPE_EFT
 extended filtering
   - 发件人: James Clark <james.clark@linaro.org>
6. **[09-01 13:40]** [PATCH v8 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>
7. **[09-01 13:40]** [PATCH v8 06/12] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
8. **[09-01 13:40]** [PATCH v8 07/12] KVM: arm64: Add trap configs for PMSDSFR_EL1
   - 发件人: James Clark <james.clark@linaro.org>
9. **[09-01 13:40]** [PATCH v8 08/12] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
10. **[09-01 13:40]** [PATCH v8 09/12] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
11. **[09-01 13:40]** [PATCH v8 10/12] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
12. **[09-01 13:40]** [PATCH v8 11/12] perf tools: Add support for
 perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
13. **[09-01 13:40]** [PATCH v8 12/12] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 6: [PATCH v2 0/6] KVM: arm64: vgic-v3: Fix yet another lock ordering turd

**📧 邮件数**: 8 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  5 Sep 2025 03:05:25 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-v3（虚拟通用中断控制器版本3）的一系列补丁，主要目的是修复锁的排序问题。

1. **原始补丁内容**：本次补丁（PATCH v2 0/6）旨在解决 vgic-v3 中的锁排序问题，具体包括对 LPI（本地中断）的引用计数管理、释放机制的改进，以及锁的使用方式的调整。

2. **之前讨论要点**：在历史讨论中，开发者们关注到 LPI 的引用计数管理不够清晰，导致在多线程环境下可能出现死锁或不安全的访问模式。补丁的初步版本（v1）已被提出，并经过初步评审。

3. **本周的新讨论与进展**：本周的讨论中，Oliver Upton 提出了补丁的多个版本（v2），并详细说明了每个补丁的变更内容，包括去除过时的注释、使用简单的引用计数、分离释放逻辑、在不需要禁用 IRQ 的情况下处理 LPI xarray 锁等。最终，这些补丁得到了 Marc Zyngier 的审查和认可，并已被应用到主线代码中。

总结来看，本次讨论集中在优化 KVM arm64 的中断处理机制，提升系统的稳定性和性能，确保在多线程环境下的安全性。

#### 📝 邮件列表

1. **[09-05 03:05]** [PATCH v2 0/6] KVM: arm64: vgic-v3: Fix yet another lock ordering turd
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-05 03:05]** [PATCH v2 1/6] KVM: arm64: vgic: Drop stale comment on IRQ active state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[09-05 03:05]** [PATCH v2 2/6] KVM: arm64: vgic-v3: Use bare refcount for VGIC LPIs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[09-05 03:05]** [PATCH v2 3/6] KVM: arm64: Spin off release helper from vgic_put_irq()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-05 03:05]** [PATCH v2 4/6] KVM: arm64: vgic-v3: Erase LPIs from xarray outside of raw spinlocks
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-05 03:05]** [PATCH v2 5/6] KVM: arm64: vgic-v3: Don't require IRQs be disabled for LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[09-05 03:05]** [PATCH v2 6/6] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may take LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[09-05 23:11]** Re: [PATCH v2 0/6] KVM: arm64: vgic-v3: Fix yet another lock ordering turd
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH v2 0/2] KVM: arm64: VHE: Debug fixes

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  2 Sep 2025 14:08:31 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的调试修复，主要涉及两个补丁（patch）。

**原始补丁内容**：
本次讨论的补丁是 v2 版本，主要包括两个部分：
1. **初始化 PMSCR_EL1**：在 KVM 启动时清零 PMSCR_EL1，以避免在 VHE 模式下意外地对来宾进行配置文件分析。
2. **正确保存和恢复主机 MDCR_EL2 值**：修复了在 vcpu 加载时未正确保存主机 MDCR_EL2 的问题。

**之前的讨论要点**：
在之前的讨论中，参与者关注了 PMSCR_EL1 和 MDCR_EL2 的初始化和保存问题，确保 KVM 在 VHE 模式下的行为一致且可预测。补丁的设计旨在解决这些潜在的调试问题。

**本周的新讨论与进展**：
本周的讨论中，Alexandru Elisei 提出了补丁的具体实现，并进行了测试，确保其在不同模式下的有效性。Oliver Upton 对补丁进行了审查，并提出了代码组织方面的建议，建议将 PMSCR_EL1 的初始化逻辑封装在一个新的函数中。最终，补丁经过讨论后被合并到修复列表中，标志着这一问题的解决。

总结来说，本次邮件讨论集中在 KVM arm64 VHE 模式下的调试修复，确保系统在不同情况下的稳定性和一致性。

#### 📝 邮件列表

1. **[09-02 14:08]** [PATCH v2 0/2] KVM: arm64: VHE: Debug fixes
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[09-02 14:08]** [PATCH v2 1/2] KVM: arm64: VHE: Initialize PMSCR_EL1
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[09-02 14:08]** [PATCH v2 2/2] KVM: arm64: VHE: Save and restore host MDCR_EL2 value correctly
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[09-03 23:55]** Re: [PATCH v2 1/2] KVM: arm64: VHE: Initialize PMSCR_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[09-03 23:55]** Re: [PATCH v2 2/2] KVM: arm64: VHE: Save and restore host MDCR_EL2
 value correctly
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[09-04 10:30]** Re: [PATCH v2 1/2] KVM: arm64: VHE: Initialize PMSCR_EL1
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[09-05 02:41]** Re: [PATCH v2 0/2] KVM: arm64: VHE: Debug fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 8: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 27 Aug 2025 17:01:49 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 Hyper-V 驱动中的 `NEED_RESCHED_LAZY` 问题，并使用通用 API 的一系列补丁（PATCH v2 0/7）。该补丁旨在解决 MSHV 根分区和上层 VTL 代码未能正确处理 `NEED_RESCHED_LAZY` 的错误，同时将与 TIF 相关的 MSHV 代码去重，将 "kvm" 入口 API 转换为更通用的 "virt" API。

在历史讨论中，Sean Christopherson 提出了多个补丁，主要包括将 KVM 相关的信号处理细节移入 KVM 本身，以消除模块依赖问题，以及将 KVM 入口代码重命名为更通用的 "virt" 以便于其他虚拟化管理程序使用。

在本周的新讨论中，Thomas Gleixner 对补丁进行了审核并表示支持。Wei Liu 更新了补丁集，去掉了 mshv_vtl 的更改，并将其余部分应用到 hyperv-next 分支。此外，Sean Christopherson 提到需要将 `mshv_do_pre_guest_mode_work()` 函数的移除与之前的补丁合并，以确保代码整洁和一致性。

总体来看，讨论进展顺利，补丁得到了积极的反馈，并在逐步完善中。

#### 📝 邮件列表

1. **[08-27 17:01]** [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-27 17:01]** [PATCH v2 4/7] entry/kvm: KVM: Move KVM details related to
 signal/-EINTR into KVM proper
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-27 17:01]** [PATCH v2 5/7] entry: Rename "kvm" entry code assets to "virt" to
 genericize APIs
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[09-02 17:41]** Re: [PATCH v2 4/7] entry/kvm: KVM: Move KVM details related to
 signal/-EINTR into KVM proper
   - 发件人: Thomas Gleixner <tglx@linutronix.de>
5. **[09-02 17:41]** Re: [PATCH v2 5/7] entry: Rename "kvm" entry code assets to "virt"
 to genericize APIs
   - 发件人: Thomas Gleixner <tglx@linutronix.de>
6. **[09-04 23:41]** Re: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common
 APIs
   - 发件人: Wei Liu <wei.liu@kernel.org>
7. **[09-04 22:39]** Re: [PATCH v2 0/7] Drivers: hv: Fix NEED_RESCHED_LAZY and use common APIs
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 9: [PATCH] KVM: arm64: Fix NULL pointer access issue

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 01 Sep 2025 18:01:45 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 NULL 指针访问问题。补丁的核心内容是添加一个条件检查 `is_kvm_arm_initialised()`，以确保 KVM 初始化完成，避免在未初始化的情况下访问每 CPU 数据，从而引发崩溃。

在历史讨论中，补丁的背景是由于在 EL1 模式下启动 Linux 时，某些情况下 KVM 的每 CPU 基指针未初始化，导致访问时出现 NULL 指针问题。补丁通过在相关函数中添加检查，确保只有在 KVM 完全初始化后才允许访问这些数据。

在本周的新讨论中，参与者对补丁进行了深入讨论。James Clark 提出，当前的 WARN_ON_ONCE() 警告不应在未初始化且不会初始化的情况下触发，建议将其移至函数的返回条件中，以便在 KVM 不可用时静默跳过相关操作。Marc Zyngier 也支持这一观点，并指出需要确保在 KVM 可用时跳过写入标志的操作。最终，Yingchao Deng 表示将根据反馈更新补丁，改善代码可读性。

总结而言，本周讨论集中在如何更合理地处理 KVM 初始化检查和错误警告，确保系统稳定性。

#### 📝 邮件列表

1. **[09-01 18:01]** [PATCH] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Yingchao Deng <yingchao.deng@oss.qualcomm.com>
2. **[09-01 11:36]** Re: [PATCH] KVM: arm64: Fix NULL pointer access issue
   - 发件人: James Clark <james.clark@linaro.org>
3. **[09-01 13:24]** Re: [PATCH] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[09-01 13:31]** Re: [PATCH] KVM: arm64: Fix NULL pointer access issue
   - 发件人: James Clark <james.clark@linaro.org>
5. **[09-01 14:30]** Re: [PATCH] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[09-01 15:16]** Re: [PATCH] KVM: arm64: Fix NULL pointer access issue
   - 发件人: James Clark <james.clark@linaro.org>
7. **[09-02 11:30]** Re: [PATCH] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Yingchao Deng (Consultant) <quic_yingdeng@quicinc.com>

---

### Thread 10: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 20 Aug 2025 15:55:20 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 的 KVM 支持的补丁系列（PATCH v10 00/43）。该补丁旨在实现受保护虚拟机的运行，相关的来宾支持已在 v6.14-rc1 中合并，因此不再需要单独处理。

在历史讨论中，Steven Price 提出了多个补丁，重点包括在 KVM 初始化时检查 RME 支持、允许虚拟机监控器（VMM）设置 RIPAS 等功能。这些补丁经过了多位开发者的审查和反馈，确保了代码的质量和功能的完整性。

在本周的新讨论中，Gavin Shan 对补丁提出了一些小的改进建议，包括代码中的冗余包含和注释位置的调整。同时，他分享了对补丁的测试结果，指出在使用特定组合启动来宾时没有明显错误，但也列出了一些已知问题，例如 virtio-iommu 不被 QEMU 支持、来宾重启命令失效等。这些问题的解决方案和信息也已与相关方共享。总的来说，本周的讨论集中在对补丁的细节优化和测试反馈上。

#### 📝 邮件列表

1. **[08-20 15:55]** [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[08-20 15:55]** [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
3. **[08-20 15:55]** [PATCH v10 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
4. **[09-03 21:15]** Re: [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Gavin Shan <gshan@redhat.com>
5. **[09-04 09:36]** Re: [PATCH v10 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
6. **[09-04 10:46]** Re: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>

---

### Thread 11: [PATCH V3 0/2] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  1 Sep 2025 12:50:35 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构中 TCR_EL1 寄存器字段宏的清理和更新，主要由 Anshuman Khandual 提出。

**原始 patch/问题的内容**：
该补丁旨在清理分散在 ARM64 平台代码（包括 KVM 实现）中的 TCR_EL1 字段宏，通过更新所需的寄存器字段定义并进行必要的替换。具体来说，TCR_XXX 宏从 `asm/pgtable-hwdef.h` 移动到 KVM 头文件 `asm/kvm_arm.h`，以便在 KVM 中继续使用。

**之前讨论要点**：
在之前的讨论中，补丁经历了几个版本的修改，主要包括修正 ARM ARM 版本、调整宏定义的类型以及删除不必要的替换。最终版本确保了功能不变，并且对 TCR_EL1 的字段进行了更新以匹配最新的 ARM 文档。

**本周的新讨论、进展或结论**：
本周的讨论中，Anshuman 提出了对 TCR_EL1 字段的进一步清理，确保宏定义的一致性。Ben Horgan 提出了对某些宏定义的疑问，认为在宏中是否包含 "EL1" 的命名会影响其位移定义。Anshuman 同意这一点，并表示将进行必要的修改以确保宏定义的正确性。此外，Anshuman 还确认了一些宏可以被完全删除，因为它们在 KVM 中并未使用，最终达成共识，确保了补丁的有效性和一致性。

#### 📝 邮件列表

1. **[09-01 12:50]** [PATCH V3 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-01 12:50]** [PATCH V3 1/2] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[09-01 12:50]** [PATCH V3 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[09-01 11:37]** Re: [PATCH V3 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[09-01 16:47]** Re: [PATCH V3 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[09-01 18:15]** Re: [PATCH V3 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 12: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 22 Aug 2025 11:18:53 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构中处理影子阶段 2 读取权限故障的补丁（patch）。该补丁旨在允许在处理影子阶段 2 时继续处理读取故障，而不是直接报错，因为在某些情况下，影子映射的权限可能与 L1 的权限不一致。

在历史讨论中，Wei-Lin Chang 提出了补丁的背景，指出在 NV（Nested Virtualization）场景下，影子映射的权限可能不如预期严格。Marc Zyngier 对此表示赞同，并提出了对 TLB（Translation Lookaside Buffer）管理的担忧，强调了在处理权限故障时需要考虑的复杂性。

在本周的新讨论中，Marc Zyngier 和 Wei-Lin Chang 进一步探讨了如何更有效地管理影子 S2 的权限。Marc 提出应始终使用来宾提供的权限，以避免在权限故障时重新遍历来宾 S2。Wei-Lin 认可了这一观点，并表示理解了如何将影子 S2 设计得更像 TLB，以便更好地指导故障处理。

总体而言，讨论集中在如何优化影子阶段 2 的权限管理，以提高虚拟化性能和稳定性。

#### 📝 邮件列表

1. **[08-22 11:18]** [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[08-22 10:40]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[08-26 21:49]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[09-01 12:06]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[09-07 17:39]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 13: [PATCH v7 05/12] arm64/boot: Factor out a macro to check SPE
 version

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 1 Sep 2025 11:05:58 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 启动代码的补丁，主题为“[PATCH v7 05/12] arm64/boot: Factor out a macro to check SPE version”。该补丁的目的是将一个用于检查 SPE（可扩展性能监控）版本的宏提取出来，以提高代码的可读性和可维护性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是对现有代码的改进，旨在优化宏的使用方式。

在本周的新讨论中，参与者主要集中在补丁的细节上。James Clark 提出了一个建议，询问是否需要将宏的定义移动到文件的开头，以便在调用之前先定义它。Leo Yan 认为虽然不是强制要求，但为了保持一致性，确实可以考虑将宏移动到文件开头。此外，讨论中还涉及到其他补丁的细节，例如对 EL2 要求的启用和对数据源过滤的支持，Leo Yan 和 James Clark 都对这些补丁表示认可，并进行了小幅修改建议。

总体来看，本周的讨论主要集中在补丁的细节和代码风格上，参与者之间的互动积极，推动了补丁的完善。

#### 📝 邮件列表

1. **[09-01 11:05]** Re: [PATCH v7 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: Leo Yan <leo.yan@arm.com>
2. **[09-01 11:19]** Re: [PATCH v7 06/12] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: Leo Yan <leo.yan@arm.com>
3. **[09-01 11:27]** Re: [PATCH v7 09/12] perf: arm_spe: Add support for filtering on
 data source
   - 发件人: Leo Yan <leo.yan@arm.com>
4. **[09-01 13:21]** Re: [PATCH v7 06/12] arm64/boot: Enable EL2 requirements for
 SPE_FEAT_FDS
   - 发件人: James Clark <james.clark@linaro.org>
5. **[09-01 13:22]** Re: [PATCH v7 05/12] arm64/boot: Factor out a macro to check SPE
 version
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 14: [PATCH] KVM: arm64: Only free fully unmapped tables in stage2_free_walker()

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  4 Sep 2025 03:17:46 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复在 `stage2_free_walker()` 函数中处理未完全映射的页表时可能导致的使用后释放（use-after-free）问题。

**原始补丁内容**：补丁的核心是修改 `stage2_free_walker()` 函数，使其仅在页表引用计数为 1 时才释放页表。这是为了避免在处理未完全映射的页表时，因过早调用 `put_page()` 而导致的错误。

**之前讨论要点**：在补丁提交之前，KVM 的实现方式是一次性遍历整个 IPA（Intermediate Physical Address）空间，可能会导致部分页表被错误释放。补丁的提出是为了修复这一问题，确保只有在页表完全未映射时才进行释放。

**本周新讨论进展**：本周的讨论中，补丁得到了积极的反馈。参与者 Marc Zyngier 和 Alexander Potapenko 分别表示已进行审核和测试，确认补丁的有效性。最终，补丁被 Oliver Upton 应用到修复分支中，标志着这一问题的解决。

#### 📝 邮件列表

1. **[09-04 03:17]** [PATCH] KVM: arm64: Only free fully unmapped tables in stage2_free_walker()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[09-05 08:31]** Re: [PATCH] KVM: arm64: Only free fully unmapped tables in stage2_free_walker()
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-05 09:37]** Re: [PATCH] KVM: arm64: Only free fully unmapped tables in stage2_free_walker()
   - 发件人: Alexander Potapenko <glider@google.com>
4. **[09-05 02:41]** Re: [PATCH] KVM: arm64: Only free fully unmapped tables in stage2_free_walker()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 15: [PATCH] arm64: kvm: Fix incorrect VNCR invalidation range calculation

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Wed,  3 Sep 2025 21:39:49 +0900

#### 🤖 AI 总结

本邮件线程讨论的主题是修复 arm64 KVM 中 VNCR 无效化范围计算的错误。原始的补丁（patch）提出了在 `kvm_invalidate_vncr_ipa()` 和 `invalidate_vncr_va()` 函数中，错误地使用了按位与运算符 `&` 和 `(size - 1)`，而应使用按位取反运算符 `~(size - 1)` 来对齐起始地址。这一错误可能导致过时的 VNCR TLB 条目在进行 TLBI 或 MMU 通知后仍然有效，从而引发内存翻译错误和意外的虚拟机行为。

在之前的讨论中，邮件参与者确认了补丁的必要性，并指出了补丁作者需要在提交时确保签名（SoB）与作者信息一致。Marc Zyngier 对补丁进行了初步审查，并表示将其应用于代码库。

本周的新讨论中，补丁作者 Dongha Lee 提交了补丁的第二版，修正了 SoB 的问题，并使用了更清晰的补丁前缀。Oliver Upton 对补丁进行了进一步审查，确认其内容良好，并要求补丁作者再次确认签名一致性。整体来看，讨论进展顺利，补丁即将被应用。

#### 📝 邮件列表

1. **[09-03 21:39]** [PATCH] arm64: kvm: Fix incorrect VNCR invalidation range calculation
   - 发件人: p@sswd.pw
2. **[09-04 10:29]** Re: [PATCH] arm64: kvm: Fix incorrect VNCR invalidation range calculation
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-05 01:16]** Re: [PATCH v2] KVM: arm64: nv: Fix incorrect VNCR invalidation range
 calculation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[09-05 17:30]** [PATCH v2] KVM: arm64: nv: Fix incorrect VNCR invalidation range calculation
   - 发件人: p@sswd.pw

---

### Thread 16: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  1 Sep 2025 23:15:51 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的嵌套虚拟化中，修复虚拟地址（VA）在 VNCR/TLBI 路径中的符号扩展问题。

**原始 patch/问题内容**：
Gyujeong Jin 提出的补丁旨在修正 VNCR/TLBI 的 VA 重建过程中，错误地将第 48 位作为符号位，而应使用第 47 位。错误的符号扩展可能导致负半部分的地址被错误地规范化，从而引发潜在的 stale VNCR 伪 TLB 条目和错误的地址转换或权限问题。

**之前讨论要点**：
在本周之前的讨论中，尚未有相关的历史讨论记录，因此没有具体的背景信息。

**本周的新讨论与进展**：
本周的讨论主要集中在补丁的细节和一些技术问题上。Marc Zyngier 对补丁的实施提出了质疑，要求进一步解释补丁中的一些表述，特别是关于“其他问题”的部分。Greg KH 则指出补丁中的签名与提交者信息不符，并提醒不要使用虚假电子邮件地址。整体来看，讨论仍在进行中，尚未达成最终结论。

#### 📝 邮件列表

1. **[09-01 23:15]** [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths
   - 发件人: Gyujeong Jin <wlsrbwjd7232@gmail.com>
2. **[09-01 15:26]** Re: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-01 22:03]** Re: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI
 paths
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
4. **[09-01 22:04]** Re: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI
 paths
   - 发件人: Greg KH <gregkh@linuxfoundation.org>

---

### Thread 17: [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Sun,  7 Sep 2025 17:59:58 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是关于对 ARM64 架构中 TCR_EL1 寄存器字段宏的清理和更新。Anshuman Khandual 提出了两个补丁（PATCH V4 0/2），旨在整合和优化 TCR_EL1 相关的宏定义，以提高代码的可维护性和一致性。

在历史讨论中，补丁的主要内容包括将分散在 ARM64 平台代码（包括 KVM 实现）中的 TCR_EL1 字段宏进行整理，并将所有必要的 TCR_XXX 宏从 `pgtable-hwdef.h` 文件移动到 KVM 头文件 `kvm_arm.h` 中，以便在 KVM 中继续使用。这一清理工作不会引入功能上的变化。

本周的新讨论中，Anshuman Khandual 更新了补丁，具体进展包括：
1. 更新 TCR_EL1 寄存器字段以符合最新的 ARM 文档，并删除了冗余的 sysreg 定义。
2. 进一步替换所有使用的 TCR_EL1 字段宏为工具 sysreg 变体，并从 `pgtable-hwdef.h` 中删除了这些宏，确保它们在 KVM 中的继续使用。

总体来看，这些补丁旨在提升代码的整洁性和一致性，同时保持现有功能不变。

#### 📝 邮件列表

1. **[09-07 17:59]** [PATCH V4 0/2] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[09-07 17:59]** [PATCH V4 1/2] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[09-07 18:00]** [PATCH V4 2/2] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH v3 00/15] KVM: Introduce KVM Userfault

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 4 Sep 2025 17:43:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM Userfault 的引入，涉及到一个名为「[PATCH v3 00/15] KVM: Introduce KVM Userfault」的补丁系列。

在历史讨论中，补丁的主要目的是为 KVM 引入用户故障处理功能，以支持更高效的虚拟机内存管理。该功能的实现将为 Firecracker 等项目提供支持，尤其是在从快照恢复 guest_memfd 支持的虚拟机时。

本周的新讨论中，Nikita Kalyazin 提出了对该补丁系列的需求，表示希望在 Firecracker 中使用 KVM Userfault 功能。James Houghton 也表示将尽快提供 QEMU 补丁，以展示 KVM Userfault 的有效性，并指出当前的主要障碍是与 kvm_page_fault 相关的内容。他承诺会在接下来的几天内审查这一系列的补丁。Sean Christopherson 进一步确认，虽然他之前没有积极推动该系列的原因是认为短期内没有需求，但现在看到 Firecracker 的兴趣后，愿意与其他人一起对接口进行对齐。

总体来看，KVM Userfault 的引入得到了积极的关注，参与者们正在努力解决相关的技术障碍，以便尽快推进该功能的实现。

#### 📝 邮件列表

1. **[09-04 17:43]** Re: [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
2. **[09-04 11:45]** Re: [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: James Houghton <jthoughton@google.com>
3. **[09-05 05:27]** Re: [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 19: [PATCH] KVM: arm64: nested: fix VNCR TLB ASID match logic for non-Global entries

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  4 Sep 2025 00:04:21 +0900

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 VNCR TLB（Translation Lookaside Buffer）ASID（Address Space Identifier）匹配逻辑，以确保非全局条目的有效性。

**原始补丁内容**：该补丁修正了 `kvm_vncr_tlb_lookup()` 函数的逻辑，使其在处理非全局条目时，只有当 ASID 匹配当前上下文时才返回真。之前的代码逻辑错误地在 ASID 不匹配时返回真，这可能导致有效条目被忽略，从而影响性能，并可能导致错误的权限故障。

**之前讨论要点**：在本周之前的讨论中并没有详细的历史记录，但补丁的必要性和潜在的安全漏洞已被提及。

**本周新讨论与进展**：本周的讨论中，Geonha Lee 提出了补丁并解释了潜在的漏洞。Marc Zyngier 对补丁表示认可，并指出在宿主机上没有立即看到漏洞，但在客户机上是显而易见的。他建议对“Reported-by”部分进行适当的归属修改。Oliver Upton 最终确认补丁已应用于修复分支，并感谢 Geonha Lee 的修复工作。整体来看，补丁得到了积极的反馈，并已被采纳。

#### 📝 邮件列表

1. **[09-04 00:04]** [PATCH] KVM: arm64: nested: fix VNCR TLB ASID match logic for non-Global entries
   - 发件人: Geonha Lee <w1nsom3gna@korea.ac.kr>
2. **[09-04 10:32]** Re: [PATCH] KVM: arm64: nested: fix VNCR TLB ASID match logic for non-Global entries
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-05 02:41]** Re: [PATCH] KVM: arm64: nested: fix VNCR TLB ASID match logic for non-Global entries
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 20: [PATCH v6 00/24] Tracefs support for pKVM

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 21 Aug 2025 09:13:48 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（[PATCH v6 00/24]），主要由 Vincent Donnefort 提出。该补丁的目的是为保护模式下的虚拟化环境提供调试和分析工具，Tracefs 被认为是理想的选择，因为它易于使用且支持多种工具。补丁系列中包括了对 Tracefs 接口的自测功能，确保其在加载、重置、大小变化和事件完整性等方面的正确性。

在历史讨论中，Vincent 提出了补丁的主要内容，并详细描述了 Tracefs 的优势及其在 pKVM 中的重要性。补丁还包括了一些自测用例，以验证 Tracefs 的功能。

在本周的新讨论中，Masami Hiramatsu 对补丁中的自测部分提出了具体建议。他建议在测试中添加“requires: remotes”以确保在未启用相关功能时跳过测试，并建议使用 $TMPDIR 代替 /tmp 作为临时工作目录。此外，他还指出了代码中存在的检查问题，建议使用 printf 来避免 checkbashisms 测试失败。

总体来看，本周的讨论集中在补丁的自测部分的改进建议上，旨在提高补丁的可靠性和兼容性。

#### 📝 邮件列表

1. **[08-21 09:13]** [PATCH v6 00/24] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[08-21 09:14]** [PATCH v6 12/24] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[09-03 13:58]** Re: [PATCH v6 12/24] tracing: selftests: Add trace remote tests
   - 发件人: Masami Hiramatsu (Google) <mhiramat@kernel.org>

---

### Thread 21: [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 20 Aug 2025 16:11:25 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 `cpu_soft_restart()` 函数中初始化 `SCTLR2_EL1` 的补丁（PATCH v3 4/5）。该补丁旨在确保在 CPU 重启时将 `SCTLR2_EL1` 设置为已知状态，以避免因当前内核的状态不确定而引发的问题。

在历史讨论中，Yeoreum Yun 提出了在初始化时应基于 ID 寄存器的建议，并讨论了在某些情况下是否需要清除 `SCTLR2_EL2`。Dave Martin 则指出，`cpu_soft_restart()` 可能在能力未启用的情况下被调用，因此需要确保在重启时 CPU 处于已知状态。

在本周的新讨论中，Dave Martin 强调了即使 `ARM64_HAS_SCTLR2` 能力未设置，也应重置 `SCTLR2_EL1`。他指出，`cpu_soft_restart()` 的职责类似于引导加载程序，应该确保 CPU 处于已知状态，特别是在处理内核崩溃时。他对 Yeoreum Yun 在 v4 版本中的重写表示认可，并表示将进一步查看该补丁。

总的来说，本周讨论的重点是确保在 CPU 重启时的状态清晰，以避免潜在的错误。

#### 📝 邮件列表

1. **[08-20 16:11]** Re: [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Dave Martin <Dave.Martin@arm.com>
2. **[08-20 18:32]** Re: [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[09-01 16:01]** Re: [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Dave Martin <Dave.Martin@arm.com>

---

### Thread 22: [PATCH v3] KVM: arm64: nv: Fix incorrect VNCR invalidation range calculation

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sat,  6 Sep 2025 13:07:24 +0900

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VNCR（Virtual Network Control Register）无效化范围计算错误的修复补丁（PATCH v3）。该补丁的主要内容是修正 `kvm_invalidate_vncr_ipa()` 和 `invalidate_vncr_va()` 函数中对起始地址对齐的错误计算，原代码使用了按位与操作（`&`）而非按位取反（`~`），导致地址位被错误地掩码，从而可能使得过时的 VNCR TLB 条目在 TLBI（Translation Lookaside Buffer Invalidate）或 MMU 通知后仍然有效，进而引发内存翻译错误和意外的客户机行为。

在之前的讨论中，未提供具体的历史背景，但本周的讨论中，补丁作者 Dongha Lee 提交了该修复补丁，并得到了 Marc Zyngier 的审核认可。Oliver Upton 在回复中确认该补丁已被应用到修复列表中，并感谢作者的贡献。

综上所述，本周的进展是该补丁成功被合并，解决了 VNCR 无效化范围计算的关键问题。

#### 📝 邮件列表

1. **[09-06 13:07]** [PATCH v3] KVM: arm64: nv: Fix incorrect VNCR invalidation range calculation
   - 发件人: p@sswd.pw
2. **[09-05 23:11]** Re: [PATCH v3] KVM: arm64: nv: Fix incorrect VNCR invalidation range calculation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 23: [PATCH] KVM: arm64: Mark freed S2 MMUs as invalid

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  5 Sep 2025 08:28:59 +0100

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: Mark freed S2 MMUs as invalid”，主要讨论了在释放 S2 MMU 时未将其标记为无效的问题。Marc Zyngier 提出，当释放 S2 MMU 及其关联的 pgd 时，如果不将该结构标记为无效，后续调用 `kvm_nested_s2_unmap()` 可能会导致尝试解除映射未分配的页表，从而引发警告。为了解决这个问题，Marc 提出了一个补丁，通过在释放 pgd 时调用 `kvm_init_nested_s2_mmu()` 来将 S2 MMU 标记为无效。

在本周的新讨论中，Marc 的补丁得到了 Oliver Upton 的认可，并已被应用到修复版本中。Oliver 表示感谢，并确认补丁的应用。这一进展表明该问题已得到及时解决，增强了 KVM 在 arm64 架构下的稳定性和可靠性。

#### 📝 邮件列表

1. **[09-05 08:28]** [PATCH] KVM: arm64: Mark freed S2 MMUs as invalid
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-05 02:41]** Re: [PATCH] KVM: arm64: Mark freed S2 MMUs as invalid
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 24: [PATCH v2] KVM: arm64: Fix NULL pointer access issue

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 02 Sep 2025 11:48:25 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个 NULL 指针访问问题的修复补丁（PATCH v2）。该补丁的主要内容是添加一个条件检查，以确保在 KVM 初始化完成之前不会访问未初始化的每 CPU 数据，防止出现 NULL 指针解引用的情况。

在历史讨论中，补丁的背景是，当 Linux 在 EL1 模式下启动时，`host_data_ptr()` 宏会解析为 nVHE（非虚拟化扩展）超管的主机数据副本。如果在 `kvm_arm_init` 中 `is_hyp_mode_available()` 返回 false，per-CPU 基指针将保持未初始化状态，从而导致访问时出现 NULL 指针错误。补丁通过添加 `is_kvm_arm_initialised()` 的条件检查来解决这一问题。

在本周的新讨论中，参与者 Oliver Upton 对补丁的短日志和变更日志提出了改进建议，认为描述应更加简洁明了，并建议将警告条件放在检查的最前面，以提高代码的可读性和安全性。Yingchao Deng 也对补丁进行了相应的修改，以增强其可读性。整体来看，本周的讨论集中在补丁的描述和代码结构优化上。

#### 📝 邮件列表

1. **[09-02 11:48]** [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Yingchao Deng <yingchao.deng@oss.qualcomm.com>
2. **[09-04 00:26]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 25: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  1 Sep 2025 21:45:20 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的嵌套虚拟化中，修复虚拟地址（VA）在 VNCR/TLBI 路径中的符号扩展问题。

本周的讨论中，Gyujeong Jin 提出了一个补丁，修改了 `read_vncr_el2` 函数中的符号扩展位数，从 48 位改为 47 位，以修复 VA 的符号扩展问题。补丁的具体修改体现在 `arch/arm64/kvm/nested.c` 文件中，涉及一行代码的插入和删除。

Marc Zyngier 对该补丁提出了质疑，询问补丁的提交信息，并指出该代码并非用于 VA 的符号扩展，而是用于在 RESS 和 BADDR 的高位传播。他提到，相关的文档 D24.2.206 中有详细说明，并强调在建立翻译时已经检查了 VA 的规范性，因此不会在这种情况下安装 TLB。Marc 还表示欢迎对补丁的进一步解释，以便更好地理解可能存在的问题。

总体来看，本周的讨论主要集中在补丁的合理性和必要性上，参与者对补丁的目的和实现细节进行了深入探讨。

#### 📝 邮件列表

1. **[09-01 21:45]** [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths
   - 发件人: Gyujeong Jin <wlsrbwjd7232@gmail.com>
2. **[09-01 14:28]** Re: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 26: [PATCH v7 00/29] KVM: arm64: Implement support for SME

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 22 Aug 2025 02:53:29 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现对 SME（Scalable Matrix Extensions）支持的补丁（PATCH v7 00/29）。该补丁的主要内容包括用户空间 ABI 的设计，特别是 SVE（Scalable Vector Extension）寄存器的向量长度、对 SVE 寄存器及 ZA 和 ZT0 的访问控制，以及针对 SME 和 SVE 的统一最终化处理。此外，还提出了类似于 FGU 的细粒度陷阱控制。

在之前的讨论中，Mark Brown 移除了补丁的 RFC（请求反馈）标签，并寻求对上述几个方面的反馈，强调了用户空间 ABI 的重要性和设计细节。

在本周的新讨论中，Marc Zyngier 建议将 QEMU 的相关人员（如 Peter Maydell 和 Eric Auger）抄送到邮件中，因为他们是使用这些 API 的关键用户。这一建议旨在确保补丁的设计能够满足实际使用者的需求，并促进更广泛的反馈与讨论。

#### 📝 邮件列表

1. **[08-22 02:53]** [PATCH v7 00/29] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-01 13:44]** Re: [PATCH v7 00/29] KVM: arm64: Implement support for SME
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 27: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 25 Aug 2025 10:39:50 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 HIP10/HIP10C 错误（erratum 162200802）提出的补丁（PATCH v2 0/4）。该补丁的主要内容是首先增加对 GICD.num_LPIs 可写支持，然后针对 HiSilicon 的错误进行修复。历史讨论中，Zhou Wang 提到在 V1 版本中存在错误，错误编号应为 162200802，并在 V2 中进行了修正。

在本周的新讨论中，Zhou Wang 再次确认了补丁系列的结构，强调首先添加 GICD.num_LPIs 的可写支持，然后再添加错误补丁。他表示如果该补丁系列得到认可，将准备与 QEMU 相关的补丁。此外，他还提供了 V1 版本的链接，以便参与者参考。

总体来看，讨论围绕修复特定硬件错误的补丁展开，强调了补丁的结构和后续工作计划。

#### 📝 邮件列表

1. **[08-25 10:39]** [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[09-01 18:55]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 28: [PATCH v5 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 18 Aug 2025 14:47:59 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 Armv8.7 新特性的补丁（PATCH v5 0/7），主要内容是引入 FEAT_{LS64, LS64_V} 特性及相关测试。这些特性涉及单副本原子64字节加载和存储指令，补丁的主要目标包括在 CPU 特性列表中添加识别和启用这些特性、通过 HWCAP3 和 cpuinfo 向用户空间暴露支持情况、增加相关的硬件能力测试，以及在虚拟机中处理不支持的内存访问陷阱。

在历史讨论中，Yicong Yang 提出了该补丁的初步版本，并强调了这些新特性的实际应用场景。讨论的重点在于如何通过 KVM/Hypervisor 处理 LS64 故障。

在本周的新讨论中，Yicong Yang 进行了跟进，询问 Marc 和 Oliver 是否认为当前版本的补丁适合继续推进。这表明讨论仍在进行中，主要集中在对 KVM/Hypvervisor 的故障处理的适当性上。整体来看，补丁的推进依然需要进一步的确认和讨论。

#### 📝 邮件列表

1. **[08-18 14:47]** [PATCH v5 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[09-01 16:08]** Re: [PATCH v5 0/7] Add support for FEAT_{LS64, LS64_V} and related
 tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>

---

### Thread 29: [PATCH] KVM: arm64: vgic: fix incorrect spinlock API usage

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun,  7 Sep 2025 13:14:13 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VGIC（虚拟通用中断控制器）代码中，修复不当使用自旋锁 API 的问题。原始的 patch 由 Alok Tiwari 提出，主要是修正 `vgic_flush_lr_state()` 函数中错误调用了 `_raw_spin_unlock()`，而应使用更为合适的 `raw_spin_unlock()`。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测出该问题的提出是基于对内核自旋锁使用规范的关注。使用低级 API `_raw_spin_unlock()` 可能导致锁的语义不正确，影响代码的稳定性和安全性。因此，修复的目的在于遵循内核的锁定约定，确保代码的正确性。

本周的讨论中，Alok Tiwari 提交了该 patch，明确指出了问题所在，并进行了相应的代码更改，替换了不当的 API 调用。此次修改在 `arch/arm64/kvm/vgic/vgic.c` 文件中进行了更新，确保了 VGIC 代码的自旋锁使用符合内核标准。该 patch 也附带了修复的引用，指向了之前的提交记录。

#### 📝 邮件列表

1. **[09-07 13:14]** [PATCH] KVM: arm64: vgic: fix incorrect spinlock API usage
   - 发件人: Alok Tiwari <alok.a.tiwari@oracle.com>

---

### Thread 30: [PATCH] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 5 Sep 2025 17:43:19 +0530

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: nv: 优化影子 S2-MMU 表的反映”，主要讨论了在 KVM（Kernel-based Virtual Machine）环境下，针对 arm64 架构的影子 S2-MMU 表进行优化的补丁。

在本周的新讨论中，参与者 Ganapatrao Kulkarni 提到他在邮件中使用了旧的 kvmarm 邮件列表 ID，并对此表示歉意。由于本邮件列表中没有历史讨论的内容，因此没有提供之前的讨论要点。

本周的讨论主要集中在补丁的提交和相关的优化内容上，虽然没有具体的技术细节或反馈，但表明了参与者对补丁的关注和对邮件列表使用的注意事项。整体来看，本周的讨论相对简短，主要是对补丁的确认和技术交流的初步启动。

#### 📝 邮件列表

1. **[09-05 17:43]** Re: [PATCH] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>

---

### Thread 31: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 1 Sep 2025 11:06:57 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持 FEAT_LSUI 特性并将其应用于 futex 原子操作的补丁（PATCH RESEND v7 0/6）。该补丁旨在提升 Linux 内核在处理 futex 时的性能和效率。

在历史讨论中，虽然没有具体的补丁内容被提及，但可以推测之前的讨论围绕着如何实现 FEAT_LSUI 特性以及其对 futex 操作的潜在影响。参与者可能探讨了该特性带来的优势，以及在内核中实现这一特性的技术细节。

在本周的新讨论中，参与者 Yeoreum Yun 发出了温和的提醒，询问是否有关于该补丁的进一步反馈。这表明该补丁仍在等待社区的关注和讨论，尚未得到明确的进展或结论。

总结来说，本邮件线程主要集中在支持 FEAT_LSUI 特性及其在 futex 原子操作中的应用，虽然没有详细的历史讨论记录，但本周的跟进显示出对该补丁的持续关注。

#### 📝 邮件列表

1. **[09-01 11:06]** Re: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: kvm-unit-tests hang on Arm FVP with protected mode

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 5 Sep 2025 17:58:45 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于在 Arm FVP 平台上运行 kvm-unit-tests 时遇到的挂起问题，特别是在使用 `kvm-arm.mode=protected` 模式时。Naresh Kamboju 提出了一个问题，指出在该模式下，kvm-unit-tests 一直挂起，而在使用 `kvm-arm.mode=vhe` 时测试能够成功完成。他通过回归分析，确定了第一个引入问题的提交为 066daa8d3bc2694c392e14091978043aed7b1f23，该提交涉及到 KVM 的 HCRX_EL2 陷阱初始化。

在本周的讨论中，Marc Zyngier 对 Naresh 的报告提出了质疑，指出 `kvm-arm.mode=vhe` 不是一个有效的选项，并要求更明确地指出哪个测试导致了失败。他还提到，提供的链接需要登录，无法访问，认为这对问题的诊断没有帮助。Mark Brown 进一步分析了日志文件，指出挂起问题可能发生在测试的第一步，并提到这个问题可能在主线代码中已经存在一段时间。

总体来看，本周的讨论集中在对问题的进一步分析和对报告内容的质疑上，尚未提出解决方案。

#### 📝 邮件列表

1. **[09-05 17:58]** kvm-unit-tests hang on Arm FVP with protected mode
   - 发件人: Naresh Kamboju <naresh.kamboju@linaro.org>
2. **[09-05 13:42]** Re: kvm-unit-tests hang on Arm FVP with protected mode
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[09-05 14:38]** Re: kvm-unit-tests hang on Arm FVP with protected mode
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 2: [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  5 Sep 2025 13:41:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 ARM64 架构下 MTE（Memory Tagging Extension）粒度掩码的补丁。补丁的主要内容是修改 MTE_GRANULE_MASK 的定义，使其在与 MTE_TAG_SHIFT 一起使用时能够生成正确的掩码。具体的代码更改是将 MTE_GRANULE_MASK 的定义从 `(~(MTE_GRANULE_SIZE - 1))` 修改为 `(MTE_GRANULE_SIZE - 1)`，以确保掩码的正确性。

在历史讨论中没有相关的背景信息，因此本周的讨论是首次提出该补丁。参与者 Vladimir Murzin 提交了补丁，并在邮件中说明了修改的目的和效果。邮件中没有提及其他参与者的反馈或进一步的讨论，因此目前尚未看到对该补丁的广泛讨论或异议。

总结而言，本周的讨论集中在修复 MTE 粒度掩码的补丁上，提供了必要的代码更改，并明确了其功能和目的。后续可能需要关注该补丁的接受情况及其对 ARM64 MTE 功能的影响。

#### 📝 邮件列表

1. **[09-05 13:41]** [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>

---

