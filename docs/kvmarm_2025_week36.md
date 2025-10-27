# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 12:15:43

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

本邮件线程讨论了针对 KVM（内核虚拟机）在 ARM64 架构上实现对 SME（可扩展矩阵扩展）的支持的补丁系列。以下是讨论的主要内容：

1. **原始补丁内容**：补丁系列的目标是为 KVM 实现对 SME 的支持，特别是在非保护的 KVM 客户端中。SME 引入了新的向量长度和控制寄存器，类似于 SVE（可扩展向量扩展），并允许在流模式下使用 SVE 寄存器。

2. **历史讨论要点**：之前的讨论集中在如何处理 SME 的用户空间 ABI、控制寄存器的访问、以及如何在 KVM 中管理 SME 状态。补丁提出了通过 KVM_ARM_VCPU_VEC 统一最终化 SVE 和 SME 的配置，以简化复杂性。

3. **本周新讨论与进展**：本周的讨论中，开发者 Mark Brown 提出了多个补丁，涵盖了 SME 寄存器的访问、状态保存与恢复、以及异常处理等方面。补丁还增加了对 SME 控制寄存器的支持，并确保在 KVM 中正确处理 SME 相关的异常。此外，补丁还更新了自测框架，以验证 SME 的实现。

总的来说，该系列补丁旨在增强 KVM 对 SME 的支持，确保在虚拟化环境中能够正确处理新的寄存器和状态，同时保持与现有 SVE 功能的兼容性。

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

本邮件讨论的主题是关于将 `set_direct_map_valid_noflush` 函数导出到 KVM 模块的补丁（PATCH v5 02/12）。该补丁的目的是为了增强 KVM 的内存管理功能，特别是在处理直接映射时的灵活性。

在历史讨论中，参与者们对补丁进行了初步审查，提出了一些修改建议，包括修正函数调用顺序和增加适当的提交描述。讨论中还涉及到其他补丁的内容，如引入 `AS_NO_DIRECT_MAP` 的补丁（PATCH v5 03/12），并对函数参数的 const 修饰符进行了探讨，确保代码的一致性和可读性。

本周的新讨论中，主要集中在对 `AS_NO_DIRECT_MAP` 补丁的进一步审查和修改上。参与者们一致认为需要保持参数的 const 一致性，以避免潜在的调试困难。此外，讨论中还提到了一些代码中的细节问题，如函数命名的清晰性和错误处理的改进。总的来说，参与者们对补丁的方向表示支持，并在细节上进行了深入的讨论和调整。

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

本邮件讨论的主题是关于 KVM 在 arm64 架构下对 GICv5 传统（GCIE_LEGACY）支持的补丁系列以及相关的清理工作。

1. **原始 patch/问题的内容**：Sascha Bischoff 提出的补丁系列旨在为基于 GICv3 的虚拟机在 GICv5 主机上启用嵌套虚拟化，并添加 CPU 功能以跟踪所有 CPU 对 FEAT_GCIE_LEGACY 的支持。此外，补丁还修复了 GICv5 主机的 ICC_SRE_EL2 访问处理，并扩展了对 vGICv3 客户的嵌套虚拟化支持。

2. **之前的讨论要点**：在历史讨论中，补丁的各个部分被逐一介绍，包括如何实现 GCIE_LEGACY 功能、修复 GIC 驱动中的标志等。参与者对补丁的设计和实现表示认可，并进行了初步的代码审查。

3. **本周的新讨论、进展或结论**：本周的讨论主要集中在对补丁的审查和反馈上。Suzuki K Poulose 和 Thomas Gleixner 对补丁表示支持并给予了审核确认。Oliver Upton 提出了针对 VGIC 的锁定问题的修复，指出了在处理 LPIs 时的锁定顺序问题，并提出了一系列补丁以优化代码结构和锁定机制。Marc Zyngier 也参与了讨论，提出了对某些实现细节的建议和修正。整体上，补丁系列得到了积极的反馈，预计将继续推进。

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

本邮件线程讨论了一个关于初始化 ARM 架构下 SCTLR2_ELx 寄存器的补丁系列（[PATCH v4 0/5]）。该补丁旨在为 Linux 提供对 SCTLR2_ELx 寄存器的初步支持，特别是在 ARMv8.8/ARMv9.3 及后续版本中，这一特性变得越来越重要。补丁的主要内容包括在 CPU 启动时初始化 SCTLR2_ELx 寄存器，以防止因寄存器未正确初始化而导致的系统异常。

在历史讨论中，Yeoreum Yun 提出了该补丁的背景，指出当前系统依赖固件初始化这些寄存器，但未来的架构特性（如 FEAT_PAuth_LR 和 FEAT_CPA2）将需要对其进行配置。补丁的具体实现包括在 CPU 启动时和 kexec 启动新内核时初始化 SCTLR2_ELx。

在本周的新讨论中，Dave Martin 对补丁提出了一些技术细节的建议，包括在汇编代码中添加错误检查和字符串比较，以确保寄存器初始化的正确性。此外，他还询问了为何 SCTLR2_ELx 的初始化顺序可能会影响系统行为，并建议在确认所有代码路径经过测试后再合并补丁。Yeoreum Yun 表示已经进行了相关测试，并确认了 SCTLR2_ELx 的值设置符合预期，尽管仍需进一步讨论和验证。整体来看，补丁的讨论进展顺利，但仍需确保其在不同场景下的有效性。

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

本邮件线程讨论了针对 ARM 架构的性能监控扩展（SPE）特性的补丁集，特别是 Armv8.8 SPE 特性。补丁集的主要内容是支持三种新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 FEAT_SPE_FDS 数据源过滤。这些特性可以独立应用，且与旧版本的性能监控工具兼容。

在历史讨论中，补丁集经历了多个版本的修改，主要集中在修复文档中的错误、优化代码结构和解决与其他内核功能的冲突。每个补丁都详细描述了其功能和实现方式。

本周的新讨论中，James Clark 提交了多个补丁，逐步实现了这些新特性的支持。例如，补丁中引入了新的配置字段 `config4`，用于支持数据源过滤，此外，还增加了对新过滤器的文档说明。参与者 Leo Yan 和其他人对补丁进行了测试和审核，确保其功能的正确性和稳定性。

整体来看，本周的进展主要是围绕新特性的实现和文档更新，确保开发者能够有效利用这些新功能。

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

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-v3（虚拟通用中断控制器）的一系列补丁，主要目的是修复锁的顺序问题。

1. **原始补丁内容**：本次补丁（PATCH v2 0/6）包含六个部分，主要针对 vgic-v3 的锁管理和 LPI（本地中断）的引用计数进行了改进。补丁的核心在于优化锁的使用，避免在不当的上下文中嵌套锁。

2. **之前讨论要点**：在历史讨论中，开发者们关注了 LPI 的引用计数管理和锁的顺序问题，指出在某些情况下可能导致死锁或不安全的操作。补丁的设计旨在解决这些潜在问题，确保在释放 LPI 时不会引发锁的冲突。

3. **本周的新讨论与进展**：本周的讨论中，Oliver Upton 提出了六个具体的补丁，逐一修复了之前提到的问题，包括去除过时的注释、使用简单的引用计数、将释放逻辑从 `vgic_put_irq()` 中分离、在不使用原始自旋锁的情况下删除 LPI、以及放宽对 LPI xarray 锁的要求。最终，这些补丁已被应用到修复分支，标志着问题的解决。

整体来看，这一系列补丁有效地改善了 KVM 在 arm64 架构下的中断管理，提升了系统的稳定性和性能。

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

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VHE（Virtualization Host Extensions）模式的调试修复补丁。

1. **原始补丁内容**：此次讨论的补丁包括两个部分：
   - 第一个补丁（PATCH v2 1/2）旨在初始化 PMSCR_EL1 寄存器，以确保在 KVM 运行时不会意外地对来宾进行性能分析。
   - 第二个补丁（PATCH v2 2/2）则修复了在 VHE 模式下保存和恢复主机 MDCR_EL2 寄存器值的逻辑。

2. **之前讨论要点**：在历史讨论中，补丁的背景主要集中在 PMSCR_EL1 和 MDCR_EL2 寄存器的处理上，强调了在不同模式下（VHE 和 nVHE）对这些寄存器的初始化和管理的必要性。

3. **本周的新讨论与进展**：本周的讨论中，Alexandru Elisei 提交了补丁的第二版，并根据 Oliver Upton 的建议进行了代码组织上的调整。Oliver 对第二个补丁进行了审核并表示支持，确认补丁已被合并到修复集中。Alexandru 也承诺将在下一次迭代中考虑进一步的代码优化。

总结而言，本周的讨论主要围绕对 KVM VHE 模式下调试寄存器处理的修复补丁，经过参与者的反馈与修改，补丁已成功应用并得到认可。

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

本邮件线程讨论的主题是关于修复 Hyper-V 驱动中的 `NEED_RESCHED_LAZY` 问题，并使用通用 API 的补丁（PATCH v2 0/7）。该补丁的主要目的是修复 MSHV 根分区和上层 VTL 代码未能正确处理 `NEED_RESCHED_LAZY` 的错误，并通过将 KVM 入口 API 转换为更通用的虚拟化 API 来去重相关代码。

在历史讨论中，Sean Christopherson 提出了多个补丁，包括将 KVM 相关的信号处理细节移入 KVM 本身，以及将 KVM 入口代码重命名为更通用的 "virt" 以便于其他虚拟化管理程序的使用。这些补丁的目标是简化代码结构并消除模块间的依赖问题。

在本周的新讨论中，Thomas Gleixner 对补丁进行了审查并表示认可。Wei Liu 通报已将大部分补丁应用到 `hyperv-next` 分支中，但指出 `mshv_do_pre_guest_mode_work()` 函数的移除未能及时处理，建议将其合并到之前的补丁中。Sean Christopherson 也确认了这一点，并表示希望将相关代码的清理工作纳入后续的补丁中。整体来看，本周的讨论主要集中在补丁的审查和后续的代码整合上。

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

本邮件线程讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 NULL 指针访问问题。补丁的主要内容是添加对 `is_kvm_arm_initialised()` 的条件检查，以确保在访问每 CPU 数据之前，KVM 已完成必要的初始化。这是因为在某些情况下，KVM 的初始化可能未完成，导致访问未初始化的指针时发生崩溃。

在之前的讨论中，参与者们关注到补丁中使用的 `WARN_ON_ONCE()` 可能会引发误报，特别是在某些情况下 KVM 不会被初始化。James Clark 提到，如果 KVM 不会运行，相关函数可以直接跳过，而不应该触发警告。Marc Zyngier 进一步指出，崩溃发生在尝试设置标志时，因此需要在 KVM 可用时跳过该操作。

本周的新讨论中，参与者们一致认为应将警告移至条件检查的最后，以提高代码的可读性。Yingchao Deng 表示将根据反馈更新补丁版本，改进代码结构。整体来看，讨论集中在如何更安全地处理 KVM 初始化及其相关函数的调用，以避免潜在的崩溃问题。

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

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 的 KVM 支持的补丁系列，主要由 Steven Price 提出，并包含 43 个补丁。补丁的核心内容是实现受保护虚拟机的运行，相关的来宾支持已在 v6.14-rc1 中合并。

在历史讨论中，Steven 提到了一些补丁的关键改动，包括修复在领域销毁时主机遍历阶段 2 页表的潜在问题，以及允许虚拟机监控器 (VMM) 在运行前设置页面状态等功能。这些补丁经过了多位开发者的审查和确认。

在本周的新讨论中，Gavin Shan 对补丁提出了一些小的改进建议，包括删除冗余的头文件引用和调整注释位置。同时，他分享了对补丁的测试结果，指出在使用特定组合启动来宾时，未发现明显错误，但也列出了几个存在的问题，例如 virtio-iommu 不被 QEMU 支持导致来宾内核在 IOMMU 探测时卡住，以及 QEMU 在执行某些命令时异常退出等。这些问题的详细信息已与相关人员共享，以便进一步解决。

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

本邮件讨论的主题是针对 ARM64 架构中的 TCR_EL1 寄存器字段宏进行清理和更新。Anshuman Khandual 提出了两个补丁（PATCH V3 0/2 和 PATCH V3 1/2），旨在将分散在 ARM64 平台代码和 KVM 实现中的 TCR_EL1 字段宏进行集中管理。补丁的主要内容包括更新寄存器字段定义，并将 TCR_XXX 宏从 `asm/pgtable-hwdef.h` 移动到 KVM 头文件 `asm/kvm_arm.h` 中，以便在 KVM 中继续使用。这一清理工作不会引入功能上的变化。

在之前的讨论中，补丁经历了多个版本的修改，主要集中在宏的表达方式和字段的准确性上。最新版本（V3）根据 Marc 的建议，采用了 TCR_EL1_XXX 的格式来表达 KVM 中的 TCR_XXX 标志。

本周的讨论中，Ben Horgan 对补丁中的某些宏定义提出了疑问，指出在移除旧宏时应确保新宏的定义仍然保持原有的逻辑。Anshuman 认可了这一点，并表示将对相关宏进行必要的调整，以确保它们的功能不受影响。最终，Anshuman 确认了一组新的宏定义，这些宏将用于 KVM，并表示将删除不再需要的宏。整体来看，本周的讨论推动了补丁的进一步完善和清晰化。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，目的是允许在处理影子二级页表（shadow stage 2）时出现读取权限故障。

**原始补丁内容**：
Wei-Lin Chang 提出的补丁旨在处理影子二级页表的读取权限故障，尽管通常情况下不应出现此类故障，但在涉及 NV（Nested Virtualization）时，可能会出现权限不一致的情况。补丁建议在处理影子二级故障时继续处理读取故障，而不是直接报错。

**之前讨论要点**：
在历史讨论中，Marc Zyngier 对补丁的逻辑表示认可，并指出 KVM 管理的 TLB（影子 S2）相对静态，因此对权限的放宽需要谨慎。他们讨论了在处理权限故障时，是否应该重新遍历来宾的二级页表，以确保获取最新的权限信息。

**本周新讨论与进展**：
在本周的讨论中，Marc Zyngier 和 Wei-Lin Chang 进一步探讨了如何更好地利用来宾提供的权限信息来简化处理流程。Marc 提出应将影子 S2 视作更类似于 TLB 的结构，以便在发生故障时直接依据影子 S2 的信息进行操作，而不是重新遍历来宾的二级页表。Wei-Lin 对此表示理解，并感谢 Marc 的解释，确认这种方法能够有效区分故障原因。

总体来看，本周的讨论推动了对补丁逻辑的深入理解，并为后续的实现提供了方向。

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

本邮件讨论的主题是关于一个针对 ARM64 引导过程的补丁（PATCH v7 05/12），该补丁的目的是将检查 SPE（可扩展性能监控）版本的宏提取出来，以提高代码的可读性和维护性。

在之前的讨论中，参与者探讨了补丁的结构和宏的定义位置。James Clark 提出了一个建议，认为将宏移动到文件开头定义会更合适，这样可以在调用之前先定义它。Leo Yan 对此表示赞同，并确认补丁的其他部分没有问题，给予了“审核通过”（Reviewed-by）的反馈。

在本周的新讨论中，Leo Yan 和 James Clark 继续讨论了其他相关补丁，包括对 EL2 要求的启用和性能监控数据源的过滤支持。James Clark 对其中一个补丁的注释提出了细微的修改建议，认为应更明确地说明“禁用对 EL2 的陷阱”。Leo Yan 也同意了这一点，并表示可以进行相应的修改。此外，Leo Yan 进一步确认了宏的定义位置并表示虽然不是强制要求，但为了保持一致性，他会将宏移动到文件开头。

总的来说，本周的讨论主要集中在补丁的细节和代码清晰度上，参与者们积极交流，确保补丁的质量和可读性。

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

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要目的是修复在 `stage2_free_walker()` 函数中出现的使用后释放（use-after-free）问题。该问题是由于在部分未映射的页表上过早调用了 `put_page()` 导致的，syzkaller 工具捕获到了这个严重的错误。

在历史讨论中，补丁的背景是 KVM 之前在处理整个 IPA（Intermediate Physical Address）空间时，执行了单一的遍历，但由于现在遍历的范围扩大到 KVM_PGTABLE_MIN_BLOCK_LEVEL，可能会导致只部分释放一个页表。为了解决这个问题，补丁修改了逻辑，仅在页表的引用计数为 1 时才释放该页表。

在本周的新讨论中，参与者们对补丁进行了积极的反馈。Marc Zyngier 对补丁进行了审核并表示认可，Alexander Potapenko 进行了测试并确认补丁有效。最终，Oliver Upton 宣布该补丁已被应用到修复分支中，标志着该问题的解决。整体来看，本周的讨论显示出社区对该补丁的支持和认可，进展顺利。

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

本邮件线程讨论了一个针对 ARM64 KVM 的补丁，旨在修复 VNCR 无效化范围计算中的错误。补丁指出，在 `kvm_invalidate_vncr_ipa()` 和 `invalidate_vncr_va()` 函数中，代码错误地使用了按位与运算符 `&` 与 `(size - 1)`，而应使用按位取反运算符 `~(size - 1)` 来对齐起始地址。这一错误可能导致过时的 VNCR TLB 条目在 TLBI 或 MMU 通知后仍然有效，从而引发内存翻译错误和意外的客户机行为。

在之前的讨论中，参与者们关注了补丁的细节和代码的准确性，特别是关于补丁提交者的签名（SoB）是否符合要求。

本周的新讨论中，补丁的提交者 DongHa Lee 提交了补丁的第二版，修正了 SoB 的不匹配问题，并且在补丁标题中增加了清晰度的前缀。参与者 Marc Zyngier 和 Oliver Upton 对补丁进行了审查，并提出了进一步的建议。Marc 对补丁表示认可，而 Oliver 则要求确保作者和 SoB 行的准确匹配。整体来看，补丁在审查过程中获得了积极反馈，预计将被应用。

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

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，旨在修复 VNCR/TLBI 路径中的虚拟地址（VA）符号扩展问题。原始补丁指出，当前的 VA 重建使用第 48 位作为符号位，但对于 48 位虚拟地址，正确的符号位应为第 47 位。错误的符号位使用可能导致负半部分地址的错误规范化，从而引发潜在的无效化遗漏和其他安全问题。

在之前的讨论中，补丁的影响被强调，包括不正确的 VA 规范化、可能的过时 VNCR 伪 TLB 条目以及在与其他问题结合时可能导致的错误翻译或权限问题。

本周的新讨论中，参与者对补丁的细节进行了深入探讨。Marc Zyngier 对补丁的某些假设提出质疑，要求更详细的解释，认为“其他问题”并不是有效的论据。同时，Greg KH 指出补丁中签名与提交者信息不一致，并提醒不要使用虚假电子邮件地址。这些讨论表明，尽管补丁的目的明确，但在技术细节和提交规范上仍需进一步澄清和修正。

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

本邮件讨论的主题是关于对 ARM64 架构中的 TCR_EL1 字段宏进行清理和更新的补丁（PATCH V4 0/2）。该补丁的主要目的是将分散在 ARM64 平台代码（包括 KVM 实现）中的 TCR_EL1 字段宏进行整理，更新所需的寄存器字段定义，并确保在 KVM 中的持续使用。

在之前的讨论中，补丁经历了多个版本的修改。V1 到 V4 的变化包括：删除未使用的 TCR_XXX 宏，将现有的 TCR_XXX 宏从 `pgtable-hwdef.h` 移动到 KVM 头文件中，并根据最新的 ARM 文档更新 TCR_EL1 寄存器字段。这些更改确保了代码的整洁性和一致性，但并不引入功能上的变化。

在本周的新讨论中，Anshuman Khandual 提出了两个补丁：第一个补丁更新了 TCR_EL1 寄存器字段以符合最新的 ARM 文档，并删除了冗余的 sysreg 定义；第二个补丁则将所有使用的 TCR_EL1 字段宏替换为工具 sysreg 变体，并从 `pgtable-hwdef.h` 中删除。整体来看，本周的讨论集中在补丁的具体实现细节上，并确认了这些更改不会影响现有功能。

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

本邮件线程讨论的主题是关于 KVM Userfault 的引入，相关的补丁为 [PATCH v3 00/15]。该补丁旨在为 KVM 提供用户故障处理功能，以支持从快照恢复基于 guest_memfd 的虚拟机。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出，之前的讨论主要集中在 KVM Userfault 的实现细节和潜在应用上。参与者们对该功能的需求表示关注，尤其是 Firecracker 项目希望利用此功能来改善其虚拟机快照恢复的能力。

在本周的新讨论中，Nikita Kalyazin 提出希望尽快合并该补丁系列，以便在 Firecracker 中实现基于 UFFD 的快照恢复功能。James Houghton 表示会尽快提供 QEMU 的补丁，以展示 KVM Userfault 的有效性。同时，他提到当前的主要障碍是与 kvm_page_fault 相关的内容，KVM Userfault 将是该 API 的首个用户。Sean Christopherson 也表示对 KVM Userfault 的实现没有概念上的问题，并强调需要对架构中立代码的接口进行协调。

总体来看，讨论的进展表明，KVM Userfault 的引入正在受到积极关注，参与者们正在努力解决相关的技术障碍，以推动该功能的实现。

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

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，旨在修复 VNCR TLB ASID 匹配逻辑，特别是针对非全局条目的处理。

**原始补丁内容**：补丁修正了 `kvm_vncr_tlb_lookup()` 函数的逻辑，使其在处理非全局条目时，只有当 ASID 匹配当前上下文时才返回真。之前的实现逻辑错误地在 ASID 不匹配时返回真，这可能导致有效条目被忽略，进而影响性能，并可能导致错误的权限故障或过时的翻译被错误地视为有效。

**之前讨论要点**：本邮件线程没有提供历史讨论的内容，因此无法总结之前的讨论要点。

**本周的新讨论和进展**：本周的讨论主要集中在补丁的有效性和潜在的安全性问题上。Marc Zyngier 对补丁表示认可，并指出在宿主机上看不到明显的漏洞，但在客户机中确实存在。Oliver Upton 确认补丁已被应用到修复列表中，并感谢 Geonha Lee 的修复工作。补丁的最终版本已被合并，链接也提供了相关的提交信息。

总结而言，此次讨论有效地解决了 VNCR TLB ASID 匹配逻辑中的问题，并得到了社区成员的认可与支持。

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

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁（PATCH v6 00/24）。该补丁旨在为在保护模式下运行的虚拟机监控器提供调试和分析工具，Tracefs 被认为是一个理想的选择，因为它易于使用和脚本化，并且支持多种工具。

在历史讨论中，Vincent Donnefort 提出了该补丁的背景，强调了 Tracefs 的优势，包括其环形缓冲区结构适合内核与虚拟机监控器之间的共享。此外，他还提交了一个具体的补丁（PATCH v6 12/24），用于增加 Tracefs 接口的自测试，以验证加载/卸载、重置、大小变化和事件完整性等功能。

在本周的新讨论中，Masami Hiramatsu 对 Vincent 提出的自测试补丁进行了反馈，建议在测试中添加“requires: remotes”以确保在未启用远程功能时跳过该测试。此外，他还建议使用 $TMPDIR 代替 /tmp 作为临时工作目录，并指出补丁中的某些代码需要使用 printf 来避免 checkbashisms 测试失败。整体来看，本周讨论集中在补丁的细节改进和测试要求上。

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

本邮件讨论的主题是关于在 `cpu_soft_restart()` 函数中初始化 `SCTLR2_EL1` 的补丁（PATCH v3 4/5）。该补丁旨在确保在软重启时将 CPU 状态重置到已知状态，无论当前内核的使用情况如何。

在历史讨论中，Yeoreum Yun 提出了在初始化时应基于 ID 寄存器进行设置的建议，尽管 Dave Martin 指出，之前的内核在未启用 `ARM64_HAS_SCTLR2` 功能时不应使用 `SCTLR2`。两位参与者讨论了在不同情况下（如 `el2_switch` 参数非零时）是否需要清除 `SCTLR2_EL2` 的问题。

在本周的新讨论中，Dave Martin 强调了即使未设置 `ARM64_HAS_SCTLR2` 功能，也应重置 `SCTLR2_EL1`。他指出，`cpu_soft_restart()` 的职责类似于引导加载程序，应该将 CPU 放入已知状态，以避免在内核崩溃时假设任何状态是合理的。他对补丁的 v4 版本表示满意，并表示将进一步查看。

总结来说，讨论围绕如何在软重启过程中确保 CPU 状态的清晰性展开，强调了在不同内核状态下的初始化必要性。

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

本邮件主题为“[PATCH v3] KVM: arm64: nv: 修复 VNCR 无效化范围计算错误”，主要讨论了在 KVM 的 arm64 架构中，VNCR 条目的无效化过程中的一个代码错误。

历史讨论部分未提供，但本周的新讨论中，Dongha Lee 提出了一个补丁，指出在 `kvm_invalidate_vncr_ipa()` 和 `invalidate_vncr_va()` 函数中，代码错误地使用了按位与操作符 `&` 与 `(size - 1)`，而应使用按位取反操作符 `~(size - 1)` 来对齐起始地址。这一错误可能导致过时的 VNCR TLB 条目在执行 TLBI 或 MMU 通知后仍然有效，从而引发内存翻译错误和意外的来宾行为。

在本周的讨论中，Oliver Upton 对该补丁表示感谢，并确认已将其应用于修复列表。补丁的具体修改涉及对 `arch/arm64/kvm/nested.c` 文件的两处代码行进行了修正，确保 VNCR 的无效化范围计算正确。

总结来说，本周的讨论集中在修复 VNCR 无效化范围计算的补丁上，确认了补丁的有效性并已被采纳。

#### 📝 邮件列表

1. **[09-06 13:07]** [PATCH v3] KVM: arm64: nv: Fix incorrect VNCR invalidation range calculation
   - 发件人: p@sswd.pw
2. **[09-05 23:11]** Re: [PATCH v3] KVM: arm64: nv: Fix incorrect VNCR invalidation range calculation
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 23: [PATCH] KVM: arm64: Mark freed S2 MMUs as invalid

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  5 Sep 2025 08:28:59 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 S2 MMU（第二级内存管理单元）释放时的一个补丁。原始补丁的目的是在释放 S2 MMU 结构时，确保将其标记为无效，以避免在后续调用 `kvm_nested_s2_unmap()` 时出现警告，因为该函数会尝试解除映射未分配的页表。

在之前的讨论中，Marc Zyngier 提出了这个补丁，指出在释放 S2 MMU 时，虽然会释放相关的 pgd（页全局目录），但未将结构标记为无效，导致后续操作可能引发错误。补丁通过调用 `kvm_init_nested_s2_mmu()` 来解决这个问题。

在本周的新讨论中，Marc Zyngier 的补丁得到了 Oliver Upton 的确认和应用，表示已将其合并到修复列表中。这标志着该问题的解决方案已被接受并实施。

#### 📝 邮件列表

1. **[09-05 08:28]** [PATCH] KVM: arm64: Mark freed S2 MMUs as invalid
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[09-05 02:41]** Re: [PATCH] KVM: arm64: Mark freed S2 MMUs as invalid
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 24: [PATCH v2] KVM: arm64: Fix NULL pointer access issue

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 02 Sep 2025 11:48:25 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM (Kernel-based Virtual Machine) 在 arm64 架构下的 NULL 指针访问问题。原始的补丁（PATCH v2）由 Yingchao Deng 提交，目的是在 Linux 启动于 EL1 模式时，确保在 KVM 初始化过程中对每个 CPU 的基础指针进行适当的初始化，以避免在访问未初始化的 per-CPU 数据时出现 NULL 指针解引用的问题。补丁通过添加对 `is_kvm_arm_initialised()` 的条件检查，确保 KVM 初始化完成所有必要步骤，包括初始化 hyp 模式。

在之前的讨论中，补丁的背景是由于在 KVM 的 trace 过滤器中，未初始化的 per-CPU 数据会导致系统崩溃。补丁的修改主要集中在改进代码的可读性，并没有改变功能。

本周的新讨论中，Oliver Upton 对补丁的简短描述和变更日志提出了批评，认为描述过于模糊，建议更清晰地表达补丁的功能变化。此外，他还建议将警告条件放在最前面，以确保在错误的上下文中调用这些帮助函数时能够及时返回。整体上，讨论集中在如何提高补丁的可读性和代码的健壮性。

#### 📝 邮件列表

1. **[09-02 11:48]** [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Yingchao Deng <yingchao.deng@oss.qualcomm.com>
2. **[09-04 00:26]** Re: [PATCH v2] KVM: arm64: Fix NULL pointer access issue
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 25: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  1 Sep 2025 21:45:20 +0900

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，旨在修复 VNCR/TLBI 路径中的虚拟地址（VA）符号扩展问题。

**原始补丁内容**：
补丁由 Gyujeong Jin 提交，修改了 `arch/arm64/kvm/nested.c` 文件中的代码，具体是将 `sign_extend64` 函数的第二个参数从 48 改为 47，以修复虚拟地址的符号扩展。

**之前讨论要点**：
本次讨论没有提供历史讨论的详细背景，但补丁的目的在于确保虚拟地址在处理过程中正确扩展，以避免潜在的错误。

**本周的新讨论与进展**：
在本周的讨论中，Marc Zyngier 对补丁提出了质疑，询问补丁的提交信息，并指出该代码并非用于虚拟地址的符号扩展，而是用于在 RESS 和 BADDR 中传播第 48 位。他提到，已经在建立翻译时检查了虚拟地址的规范性，因此在这种情况下不会安装 TLB。Marc Zyngier 还表示，如果 Gyujeong Jin发现了他未注意到的问题，欢迎进一步解释。

总结来看，本周的讨论主要集中在对补丁目的和实现细节的质疑上，尚未达成共识。

#### 📝 邮件列表

1. **[09-01 21:45]** [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths
   - 发件人: Gyujeong Jin <wlsrbwjd7232@gmail.com>
2. **[09-01 14:28]** Re: [PATCH] KVM: arm64: nested: Fix VA sign extension in VNCR/TLBI paths
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 26: [PATCH v7 00/29] KVM: arm64: Implement support for SME

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 22 Aug 2025 02:53:29 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现对 SME（Scalable Matrix Extension）支持的补丁（PATCH v7 00/29）。该补丁旨在改进用户空间 ABI，特别是涉及 SVE（Scalable Vector Extension）寄存器的向量长度、访问方式以及对 ZA 和 ZT0 的控制，此外还包括对细粒度陷阱的控制。

在历史讨论中，Mark Brown 提出了需要反馈的几个关键点，包括用户空间 ABI 的设计和 SVE、SME 的最终化处理方式。虽然 RFC 标签已被移除，但他仍在寻求社区的意见和建议。

在本周的新讨论中，Marc Zyngier 建议将 QEMU 团队的相关人员（如 Peter Maydell 和 Eric Auger）抄送到邮件中，因为他们是使用这些 API 的关键参与者。这一建议表明了对补丁影响范围的关注，并希望通过更广泛的反馈来完善补丁的设计。

#### 📝 邮件列表

1. **[08-22 02:53]** [PATCH v7 00/29] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[09-01 13:44]** Re: [PATCH v7 00/29] KVM: arm64: Implement support for SME
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 27: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 25 Aug 2025 10:39:50 +0800

#### 🤖 AI 总结

本邮件线程讨论了针对 HIP10/HIP10C 错误（erratum 162200802）的补丁（patch）问题。历史讨论中，Zhou Wang 提出了补丁的第二版（v2），该补丁首先增加了 GICD.num_LPIs 的可写支持，然后针对 HiSilicon 的错误进行了修复。补丁中还修正了在第一版（v1）中错误的错误编号，确保其为 162200802。

在本周的新讨论中，Zhou Wang 再次确认了补丁系列的结构，强调该系列首先添加了 GICD.num_LPIs 的可写支持，随后是针对错误的补丁。他表示如果该系列得到认可，将会准备与 QEMU 相关的补丁。此外，他还提供了 v1 版本的链接，以便参与者参考。

总体而言，讨论集中在对补丁的确认和后续工作的计划上，显示出对解决该错误的持续关注。

#### 📝 邮件列表

1. **[08-25 10:39]** [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[09-01 18:55]** Re: [PATCH v2 0/4] Add workaround for HIP10/HIP10C erratum 162200802
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 28: [PATCH v5 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 18 Aug 2025 14:47:59 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于支持 Armv8.7 中的 FEAT_{LS64, LS64_V} 特性的补丁（PATCH v5 0/7）。该补丁旨在引入单拷贝原子 64 字节加载和存储指令，具体内容包括在 CPU 特性列表中添加识别和启用功能、通过 HWCAP3 和 cpuinfo 向用户空间暴露这些特性支持、添加相关的硬件能力测试，以及在虚拟机中处理不支持的内存访问的陷阱。

在历史讨论中，Yicong Yang 提出了该补丁的初步版本，并强调了这些新特性在虚拟化环境中的重要性，尤其是在 KVM/hypervisor 中的故障处理。

在本周的新讨论中，Yicong Yang 对之前的讨论进行了跟进，询问 Marc 和 Oliver 是否认为当前版本的补丁可以继续推进。讨论的重点仍然集中在 LS64 特性的故障处理上，表明该问题仍需进一步澄清和确认。整体来看，补丁的推进依赖于对 KVM/hypervisor 中相关处理的认可和完善。

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

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic（虚拟通用中断控制器）代码中，修复不当使用自旋锁 API 的问题。

在本周的讨论中，Alok Tiwari 提出了一个补丁（patch），该补丁修正了函数 `vgic_flush_lr_state()` 中对 `_raw_spin_unlock()` 的调用，改为使用适当的 `raw_spin_unlock()`。_raw_spin_unlock() 是一个内部低级 API，不应直接使用，而使用 raw_spin_unlock() 可以确保在 vgic 代码中的正确锁定语义。此更改旨在避免误用内部函数，并与内核锁定约定保持一致。

补丁的提交信息中提到，此次修复是针对之前提交的一个更改（8fa3adb8c6be），该更改将 `vgic_irq->irq_lock` 设置为 raw_spinlock。邮件中仅包含这一条新讨论，没有涉及历史讨论的内容。

#### 📝 邮件列表

1. **[09-07 13:14]** [PATCH] KVM: arm64: vgic: fix incorrect spinlock API usage
   - 发件人: Alok Tiwari <alok.a.tiwari@oracle.com>

---

### Thread 30: [PATCH] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 5 Sep 2025 17:43:19 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于优化 KVM（Kernel-based Virtual Machine）在 arm64 架构下的影子 S2-MMU 表的反映（unmapping）过程。Ganapatrao Kulkarni 提出了一个补丁（patch），旨在提高这一过程的效率。

在历史讨论部分，由于没有相关的邮件记录，因此无法提供更多背景信息或之前的讨论要点。

在本周的新讨论中，Ganapatrao Kulkarni 对补丁进行了说明，并为使用旧的 kvmarm 邮件列表 ID 表达了歉意。这表明他在提交补丁时可能遇到了一些技术问题，但具体的讨论内容尚未展开。

总体来看，本周的讨论主要集中在补丁的提交和邮件列表使用上，尚未深入探讨补丁的具体实现或效果。

#### 📝 邮件列表

1. **[09-05 17:43]** Re: [PATCH] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>

---

### Thread 31: [PATCH RESEND v7 0/6] support FEAT_LSUI and apply it on futex
 atomic ops

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 1 Sep 2025 11:06:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 FEAT_LSUI 并将其应用于 futex 原子操作的补丁（patch）。该补丁旨在提升 Linux 内核中对 futex 的性能和效率。

在历史讨论中，虽然没有具体的邮件内容提供，但可以推测之前的讨论可能集中在 FEAT_LSUI 的功能及其对 futex 操作的潜在影响上。FEAT_LSUI 是一种新的硬件特性，能够优化原子操作的执行。

本周的讨论中，参与者 Yeoreum Yun 发送了一封邮件，提醒其他人关注该补丁的进展，表明可能存在对该补丁的进一步讨论或反馈的期待。邮件中没有提供新的技术细节或进展，主要是对之前讨论的跟进。

总结而言，本邮件线程的核心是对支持 FEAT_LSUI 的补丁的关注，尽管目前没有新的技术进展，但参与者希望能引起更多的讨论和反馈。

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

本邮件讨论的主题是关于在 Arm FVP 上运行 kvm-unit-tests 时出现的挂起问题，特别是在使用 `kvm-arm.mode=protected` 模式时。

1. **原始问题**：Naresh Kamboju 报告称，在 Arm FVP 上使用 `kvm-arm.mode=protected` 启动 kvm-unit-tests 时，测试会持续挂起，而使用 `kvm-arm.mode=vhe` 则能够成功完成测试。经过回溯，发现导致问题的第一个坏提交是 066daa8d3bc2694c392e14091978043aed7b1f23，涉及到 KVM 的 HCRX_EL2 陷阱初始化。

2. **之前讨论要点**：本周的讨论没有历史背景，但 Naresh 提供了详细的测试环境信息，包括平台、内核版本和测试命令行参数，强调了问题的可重现性。

3. **本周的新讨论和进展**：Marc Zyngier 对 Naresh 的报告提出了质疑，指出 `kvm-arm.mode=vhe` 不是一个有效的选项，并要求更明确地指出哪个测试触发了失败。Mark Brown 进一步分析了日志文件，认为挂起发生在测试的第一步，指出可能是 "selftest-setup" 测试失败。由于 Marc 的 Linaro 账户被禁用，他无法访问相关的日志文件，这可能影响到主线版本的稳定性。

整体来看，本周的讨论集中在对问题的进一步分析和对报告内容的质疑上，尚未达成明确的解决方案。

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

本邮件主题为“[kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask”，由 Vladimir Murzin 提交。该补丁的主要目的是修复 ARM64 架构中 MTE（Memory Tagging Extension）相关的 granule mask，使其在与 MTE_TAG_SHIFT 一起使用时能够生成正确的掩码。

在本周的讨论中，Vladimir Murzin 提交了该补丁，具体修改了 arm/mte.c 文件中的 MTE_GRANULE_MASK 定义。之前的定义使用了不正确的位运算，导致生成的掩码不符合预期。补丁通过将 MTE_GRANULE_MASK 的定义改为“(MTE_GRANULE_SIZE - 1)”来修正这一问题。

本周的讨论没有涉及其他参与者的回复或进一步的讨论，主要集中在补丁的内容和必要性上。补丁的提交标志着对 MTE 功能的进一步完善，确保了在使用 MTE 标签时的正确性。

#### 📝 邮件列表

1. **[09-05 13:41]** [kvm-unit-tests PATCH] arm64: mte: Fix MTE granule mask
   - 发件人: Vladimir Murzin <vladimir.murzin@arm.com>

---

