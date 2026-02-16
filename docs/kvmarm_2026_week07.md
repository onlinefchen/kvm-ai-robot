# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-02-16 00:30:45

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 144
- **总 Thread 数**: 23
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 19 threads (131 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 2 threads (2 邮件)
- **Other**: 1 threads (9 邮件)

---

## 📌 PATCH

共 19 个 thread

---

### Thread 1: [PATCH v6 00/19] ARM64 PMU Partitioning

**📧 邮件数**: 29 | **👥 参与者**: 3 | **📅 开始时间**: Mon,  9 Feb 2026 22:13:55 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 平台的 PMU（性能监控单元）分区的补丁系列，主要由 Colton Lewis 提出。以下是该讨论的总结：

1. **原始补丁内容**：
   本次补丁系列（[PATCH v6 00/19]）旨在实现 ARM64 的分区 PMU 方案，允许为虚拟机保留部分计数器，从而减少性能开销。补丁中包括了对 PMU 相关寄存器的访问优化和动态计数器保留的实现。

2. **历史讨论要点**：
   之前的讨论集中在如何实现 PMU 的分区功能，特别是如何在 VHE（虚拟化扩展）模式下支持这一特性。参与者们讨论了 PMU 的寄存器访问、上下文切换的效率以及如何处理中断等问题。

3. **本周新讨论与进展**：
   - 本周的讨论中，Colton 提出了多个补丁，涵盖了 PMU 的寄存器处理、事件过滤、上下文切换等方面的实现。特别是引入了对 PMU 寄存器的快速路径处理，以提高性能。
   - Marc Zyngier 提出了一些批评意见，认为缺乏用户空间如何使用这一功能的示例，认为这是评审的一个阻碍。他强调需要提供更清晰的用户空间接口示例，以便更好地理解 PMU 分区的使用。
   - 讨论中还提到，虽然自测用例存在，但并未充分展示如何配置 PMU，因此建议提供 QEMU 或其他 VMM 的示例代码。

总之，本周的讨论围绕着 PMU 分区的实现细节、性能优化以及如何在用户空间中有效使用这些功能展开，强调了提供具体示例的重要性。

#### 📝 邮件列表

1. **[02-09 22:13]** [PATCH v6 00/19] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[02-09 22:13]** [PATCH v6 01/19] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[02-09 22:13]** [PATCH v6 02/19] KVM: arm64: Reorganize PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[02-09 22:13]** [PATCH v6 03/19] KVM: arm64: Reorganize PMU functions
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[02-09 22:13]** [PATCH v6 04/19] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[02-09 22:14]** [PATCH v6 05/19] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[02-09 22:14]** [PATCH v6 06/19] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[02-09 22:14]** [PATCH v6 07/19] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[02-09 22:14]** [PATCH v6 08/19] KVM: arm64: Define access helpers for PMUSERENR and PMSELR
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[02-09 22:14]** [PATCH v6 09/19] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[02-09 22:14]** [PATCH v6 10/19] KVM: arm64: Setup MDCR_EL2 to handle a partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
12. **[02-09 22:14]** [PATCH v6 11/19] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
13. **[02-09 22:14]** [PATCH v6 12/19] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[02-09 22:14]** [PATCH v6 13/19] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[02-09 22:14]** [PATCH v6 14/19] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[02-09 22:14]** [PATCH v6 15/19] KVM: arm64: Detect overflows for the Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[02-09 22:14]** [PATCH v6 16/19] KVM: arm64: Add vCPU device attr to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
18. **[02-09 22:14]** [PATCH v6 17/19] KVM: selftests: Add find_bit to KVM library
   - 发件人: Colton Lewis <coltonlewis@google.com>
19. **[02-09 22:14]** [PATCH v6 18/19] KVM: arm64: selftests: Add test case for partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
20. **[02-09 22:14]** [PATCH v6 19/19] KVM: arm64: selftests: Relax testing for exceptions
 when partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
21. **[02-10 12:30]** Re: [PATCH v6 08/19] KVM: arm64: Define access helpers for PMUSERENR
 and PMSELR
   - 发件人: kernel test robot <lkp@intel.com>
22. **[02-10 12:51]** Re: [PATCH v6 14/19] perf: arm_pmuv3: Handle IRQs for Partitioned
 PMU guest counters
   - 发件人: kernel test robot <lkp@intel.com>
23. **[02-10 13:20]** Re: [PATCH v6 08/19] KVM: arm64: Define access helpers for PMUSERENR
 and PMSELR
   - 发件人: kernel test robot <lkp@intel.com>
24. **[02-10 13:55]** Re: [PATCH v6 16/19] KVM: arm64: Add vCPU device attr to partition
 the PMU
   - 发件人: kernel test robot <lkp@intel.com>
25. **[02-10 15:32]** Re: [PATCH v6 14/19] perf: arm_pmuv3: Handle IRQs for Partitioned
 PMU guest counters
   - 发件人: kernel test robot <lkp@intel.com>
26. **[02-10 08:49]** Re: [PATCH v6 00/19] ARM64 PMU Partitioning
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[02-12 09:07]** Re: [PATCH v6 09/19] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[02-12 21:08]** Re: [PATCH v6 00/19] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
29. **[02-13 08:11]** Re: [PATCH v6 00/19] ARM64 PMU Partitioning
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 28 | **👥 参与者**: 6 | **📅 开始时间**: Tue,  3 Feb 2026 21:43:01 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM MPAM（内存带宽分配管理）与 KVM/arm64 及 resctrl 之间的集成，主要涉及一系列补丁（PATCH v4 00/41）。

**原始补丁内容**：
补丁旨在为 ARM MPAM 提供 KVM/arm64 和 resctrl 的支持，包含多个重要的功能改进和修复。补丁中加强了特性暴露的启发式判断，以避免不必要的资源承诺，并删除了需要 resctrl 支持的 ABMC 模拟。

**之前讨论要点**：
历史讨论中，参与者们关注了 MPAM 驱动的不同功能实现，包括对缓存类型的选择、重置控制的实现以及对 CDP（缓存数据优先）功能的支持等。讨论中提到，MPAM 驱动需与 resctrl 进行有效的集成，以确保资源的正确管理和分配。

**本周新讨论与进展**：
本周的讨论中，参与者们对补丁进行了详细的审查和反馈。Fenghua Yu 提出需要更正文档中的 ARM 和 x86 的描述。Shaopeng Tan 询问了 ABMC 的计数器分配部分的必要性，并得到了 Ben Horgan 的详细解释。Zeng Heng 对 MPAM 功能进行了测试，确认了多个功能的正常运行，并提出了对 MBW_MIN 值的行为解释，认为其总和超过100%是可接受的。此外，Reinette Chatre 和其他参与者对代码中的一些实现细节提出了改进建议，确保系统在不同资源支持下的稳定性。

总的来看，邮件讨论围绕 ARM MPAM 的补丁系列进行了深入的技术交流，参与者们积极反馈并提出改进建议，推动了补丁的完善与实施。

#### 📝 邮件列表

1. **[02-03 21:43]** [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[02-03 21:43]** [PATCH v4 13/41] arm_mpam: resctrl: Add boilerplate cpuhp and domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[02-03 21:43]** [PATCH v4 15/41] arm_mpam: resctrl: Pick the caches we will use as resctrl resources
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[02-03 21:43]** [PATCH v4 16/41] arm_mpam: resctrl: Implement resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[02-03 21:43]** [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[02-03 21:43]** [PATCH v4 20/41] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[02-03 21:43]** [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[02-03 21:43]** [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[02-05 16:50]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB'
 resource
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
10. **[02-08 17:16]** Re: [PATCH v4 20/41] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>
11. **[02-09 08:25]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
12. **[02-09 10:04]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
13. **[02-09 15:36]** Re: [PATCH v4 20/41] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[02-10 06:20]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
15. **[02-10 14:57]** Re: [PATCH v4 13/41] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
16. **[02-10 15:39]** Re: [PATCH v4 15/41] arm_mpam: resctrl: Pick the caches we will use
 as resctrl resources
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
17. **[02-11 10:50]** Re: [PATCH v4 20/41] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[02-11 11:05]** Re: [PATCH v4 15/41] arm_mpam: resctrl: Pick the caches we will use
 as resctrl resources
   - 发件人: Ben Horgan <ben.horgan@arm.com>
19. **[02-11 15:36]** Re: [PATCH v4 13/41] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
20. **[02-12 14:51]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[02-12 08:22]** Re: [PATCH v4 15/41] arm_mpam: resctrl: Pick the caches we will use
 as resctrl resources
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
22. **[02-13 11:32]** Re: [PATCH v4 16/41] arm_mpam: resctrl: Implement
 resctrl_arch_reset_all_ctrls()
   - 发件人: Zeng Heng <zengheng4@huawei.com>
23. **[02-13 07:02]** Re: [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
24. **[02-13 07:18]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
25. **[02-13 15:38]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Zeng Heng <zengheng4@huawei.com>
26. **[02-14 09:29]** Re: [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Zeng Heng <zengheng4@huawei.com>
27. **[02-14 17:40]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Zeng Heng <zengheng4@huawei.com>
28. **[02-14 18:39]** Re: [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update
 configuration
   - 发件人: Zeng Heng <zengheng4@huawei.com>

---

### Thread 3: [PATCH v12 0/7] support FEAT_LSUI

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 6 Feb 2026 09:04:41 +0000

#### 🤖 AI 总结

本邮件线程讨论了支持 ARM 架构中的 FEAT_LSUI 特性的补丁系列（PATCH v12 0/7）。该补丁旨在为 ARM64 架构添加对 FEAT_LSUI 的支持，涉及多个方面的修改，包括 Kconfig 配置和 CPU 特性处理。

在历史讨论中，参与者 Yeoreum Yun 提出了补丁，并得到了 Catalin Marinas 的初步反馈，指出由于合并窗口即将开启，该补丁的优先级较低，计划在下一个周期进行合并。同时，Catalin 提到在补丁的实现中，Kconfig 的添加应放在最后以便于版本回溯。

本周的新讨论中，Catalin 和 Yeoreum 针对补丁中的依赖关系进行了深入探讨。Catalin 提出，由于在 7.0 版本中移除了 CONFIG_ARM64_PAN，导致禁用的复杂性增加，建议在实现中添加额外的检查以确保兼容性。Yeoreum 则表示对 FEAT_LSUI 和 FEAT_PAN 的依赖关系存在疑问，并提出可以简化代码逻辑，避免引入新的函数。双方还讨论了如何处理与 SW_PAN 兼容性的问题，并就代码的可读性和简洁性进行了多次交流。

总体来看，本周的讨论集中在补丁的实现细节和代码优化上，参与者们积极提出建议，推动补丁的完善。

#### 📝 邮件列表

1. **[02-06 09:04]** Re: [PATCH v12 0/7] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[02-06 18:35]** Re: [PATCH v12 0/7] support FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[02-06 18:36]** Re: [PATCH v12 1/7] arm64: Kconfig: add support for LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[02-06 18:42]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[02-09 18:57]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-10 09:54]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[02-10 09:56]** Re: [PATCH v12 1/7] arm64: Kconfig: add support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[02-10 16:14]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[02-10 16:45]** Re: [PATCH v12 6/7] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[02-10 17:01]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[02-10 17:17]** Re: [PATCH v12 6/7] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
12. **[02-12 08:08]** Re: [PATCH v12 0/7] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 4: [PATCH v1 0/3] KVM: arm64: Fix guest feature sanitization and pKVM
 state synchronization

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 12 Feb 2026 09:02:49 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁系列，主要集中在修复来宾特性消毒和 pKVM 状态同步的问题。

**原始补丁内容**：
补丁系列包括三个部分：
1. **补丁 1**：修复 KVM 中的 FEAT_S1POE 特性在主机未启用 CONFIG_ARM64_POE 时错误地暴露给来宾的问题。
2. **补丁 2**：修复非保护模式下 pKVM 来宾初始化时 ID 寄存器未正确复制的问题，导致特性检查失败。
3. **补丁 3**：移除 unpin_host_sve_state() 中冗余的 kern_hyp_va() 调用。

**之前讨论要点**：
在历史讨论中，未提及具体的讨论内容，但补丁的背景是为了确保超管在上下文切换时正确处理架构扩展，以防止状态损坏。参与者对此补丁的必要性和实现细节进行了探讨。

**本周的新讨论与进展**：
本周的讨论主要围绕补丁的具体实现和潜在问题。Fuad Tabba 提出了补丁的细节，并与 Marc Zyngier 讨论了如何更好地处理特性暴露和状态初始化的问题。Marc 提出了一些改进建议，如在配置选项未启用时是否应有默认覆盖，以确保 KVM 的一致性。最终，Fuad 同意在应用补丁时移除某些冗余更改，并计划根据讨论的反馈进行进一步修正。

整体来看，本周的讨论集中在补丁的细节和实现的合理性上，参与者积极交流以确保补丁的有效性和稳定性。

#### 📝 邮件列表

1. **[02-12 09:02]** [PATCH v1 0/3] KVM: arm64: Fix guest feature sanitization and pKVM
 state synchronization
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-12 09:02]** [PATCH v1 1/3] KVM: arm64: Hide S1POE from guests when not supported
 by the host
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-12 09:02]** [PATCH v1 2/3] KVM: arm64: Fix ID register initialization for
 non-protected pKVM guests
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-12 09:02]** [PATCH v1 3/3] KVM: arm64: Remove redundant kern_hyp_va() in unpin_host_sve_state()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[02-12 09:29]** Re: [PATCH v1 1/3] KVM: arm64: Hide S1POE from guests when not supported by the host
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-12 09:41]** Re: [PATCH v1 1/3] KVM: arm64: Hide S1POE from guests when not
 supported by the host
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[02-12 15:35]** Re: [PATCH v1 1/3] KVM: arm64: Hide S1POE from guests when not supported by the host
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-12 18:53]** Re: [PATCH v1 1/3] KVM: arm64: Hide S1POE from guests when not
 supported by the host
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[02-13 10:40]** Re: [PATCH v1 1/3] KVM: arm64: Hide S1POE from guests when not supported by the host
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-13 11:03]** Re: [PATCH v1 2/3] KVM: arm64: Fix ID register initialization for non-protected pKVM guests
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-13 11:07]** Re: [PATCH v1 2/3] KVM: arm64: Fix ID register initialization for
 non-protected pKVM guests
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 5: [PATCH kvmtool v6 0/6] arm64: Nested virtualization support

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 11 Feb 2026 13:12:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于为 ARM64 架构的 KVM 工具添加嵌套虚拟化支持的补丁系列（v6 版本）。该补丁系列的主要内容包括修复维护 IRQ 代码中的字节序错误，并对补丁进行了重整。

在之前的讨论中，补丁系列的目标是实现 ARMv8.3 架构的嵌套虚拟化支持，允许用户通过命令行选项 `--nested` 启动虚拟机（VCPU）在 EL2 模式下运行。此外，补丁还引入了 VGIC 支持、计数器偏移控制、以及对 FEAT_E2H0 的支持等功能。

本周的新讨论中，Andre Przywara 和 Marc Zyngier 提出了多个补丁，具体包括：
1. **补丁 1**：引入 `--nested` 选项以支持在 EL2 启动 VCPU。
2. **补丁 2**：添加维护 IRQ 的设置支持。
3. **补丁 3**：添加计数器偏移控制选项。
4. **补丁 4**：支持 FEAT_E2H0，以便在不支持 VHE 的情况下运行旧版操作系统。
5. **补丁 5**：生成 HYP 定时器中断说明符。
6. **补丁 6**：处理在嵌套虚拟化下的 virtio 字节序重置问题。

讨论中提到的一个问题是，SCTLR_EL1 和 EL2 的编码相同，这可能导致在 EL1 客户机上引入回归错误。整体来看，补丁系列的进展顺利，嵌套虚拟化的支持逐步完善。

#### 📝 邮件列表

1. **[02-11 13:12]** [PATCH kvmtool v6 0/6] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[02-11 13:12]** [PATCH kvmtool v6 1/6] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[02-11 13:12]** [PATCH kvmtool v6 2/6] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[02-11 13:12]** [PATCH kvmtool v6 3/6] arm64: Add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[02-11 13:12]** [PATCH kvmtool v6 4/6] arm64: Add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[02-11 13:12]** [PATCH kvmtool v6 5/6] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[02-11 13:12]** [PATCH kvmtool v6 6/6] arm64: Handle virtio endianness reset when running nested
   - 发件人: Andre Przywara <andre.przywara@arm.com>
8. **[02-11 14:08]** Re: [PATCH kvmtool v6 6/6] arm64: Handle virtio endianness reset when running nested
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v11 00/30] Tracefs support for pKVM

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 31 Jan 2026 13:28:18 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁（PATCH v11 00/30），旨在为受保护模式下的虚拟化提供调试和分析工具。该补丁系列引入了 Tracefs，因其易用性和与多种工具的兼容性而被认为是理想的选择。补丁内容包括添加非消耗性读取功能和自测试功能，以验证 Tracefs 接口的有效性。

在历史讨论中，参与者 Vincent Donnefort 提出了多个补丁，涉及 Tracefs 的实现细节和自测试用例。Steven Rostedt 对补丁中的某些实现提出了疑问，尤其是关于迭代器的空值处理和锁的管理。

在本周的新讨论中，Vincent 和 Steven 继续探讨补丁的细节，Steven 指出在处理迭代器时的逻辑问题，并提出了改进建议。同时，他还提到在某些测试中遇到的问题，尤其是与 CPU 下线操作相关的测试未能如预期工作。

总体而言，本周的讨论集中在补丁的细节修正和测试用例的有效性上，参与者们积极交流以确保补丁的质量和功能完整性。

#### 📝 邮件列表

1. **[01-31 13:28]** [PATCH v11 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[01-31 13:28]** [PATCH v11 07/30] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[01-31 13:28]** [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-04 18:52]** Re: [PATCH v11 07/30] tracing: Add non-consuming read to trace
 remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
5. **[02-05 12:42]** Re: [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
6. **[02-10 15:32]** Re: [PATCH v11 07/30] tracing: Add non-consuming read to trace
 remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[02-10 15:54]** Re: [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 7: [PATCH v2 0/4] KVM: arm64: Fix guest feature sanitization and pKVM
 state synchronization

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 13 Feb 2026 14:38:11 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下的补丁系列，主要关注于修复来宾特性消毒和 pKVM 状态同步的问题。

**原始补丁内容**：
该补丁系列旨在解决标准 KVM 和 pKVM 实现中的状态管理和特性同步漏洞，确保在上下文切换时，虚拟机监控器（hypervisor）正确处理架构扩展，以防止状态损坏。

**之前讨论要点**：
在历史讨论中并未提及具体的补丁或问题背景，但本周的讨论明确指出了补丁的目的和重要性，尤其是在处理未支持特性的情况下，如何避免将这些特性暴露给来宾。

**本周的新讨论与进展**：
本周的讨论中，Fuad Tabba 提出了四个补丁，具体包括：
1. 隐藏未被主机支持的 S1POE 特性，防止来宾访问。
2. 优化对未支持 S1POE 的处理，确保编译器能够消除相关代码路径。
3. 修复非保护模式下的 ID 寄存器初始化问题，确保特性检测逻辑正常工作。
4. 移除在 `unpin_host_sve_state()` 中多余的 `kern_hyp_va()` 调用。

最后，Marc Zyngier 确认已将这些补丁应用到修复集，表明讨论取得了积极进展。

#### 📝 邮件列表

1. **[02-13 14:38]** [PATCH v2 0/4] KVM: arm64: Fix guest feature sanitization and pKVM
 state synchronization
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-13 14:38]** [PATCH v2 1/4] KVM: arm64: Hide S1POE from guests when not supported
 by the host
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-13 14:38]** [PATCH v2 2/4] KVM: arm64: Optimise away S1POE handling when not
 supported by host
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-13 14:38]** [PATCH v2 3/4] KVM: arm64: Fix ID register initialization for
 non-protected pKVM guests
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[02-13 14:38]** [PATCH v2 4/4] KVM: arm64: Remove redundant kern_hyp_va() in unpin_host_sve_state()
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[02-13 14:58]** Re: [PATCH v2 0/4] KVM: arm64: Fix guest feature sanitization and pKVM state synchronization
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v2 07/35] KVM: arm64: Remove is_protected_kvm_enabled()
 checks from hypercalls

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 10 Feb 2026 14:53:15 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要内容是移除 hypercalls 中对 `is_protected_kvm_enabled()` 的检查。

在历史讨论中，补丁的目标是简化 hypercall 的实现，特别是针对 pKVM（Protected Kernel Virtual Machine）功能的支持。参与者 Will Deacon 提出了一些关于代码注释和函数命名的建议，认为现有的注释可能会误导开发者对函数的理解。

本周的新讨论中，Alexandru Elisei 对补丁提出了具体的疑问，询问了某些 hypercall 的处理逻辑，并建议在代码中使用更一致的命名。此外，Trilok Soni 和 Fuad Tabba 讨论了如何在 QEMU 环境中测试该补丁，确认 QEMU 可以正常工作，但需要使用特定的 kvmtool 补丁。

总体来看，本周的讨论集中在对补丁的细节审查、代码命名一致性以及测试环境的可行性上，参与者们积极交流以确保补丁的质量和可用性。

#### 📝 邮件列表

1. **[02-10 14:53]** Re: [PATCH v2 07/35] KVM: arm64: Remove is_protected_kvm_enabled()
 checks from hypercalls
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[02-10 10:58]** Re: [PATCH v2 00/35] KVM: arm64: Add support for protected guest
 memory with pKVM
   - 发件人: Trilok Soni <trilokkumar.soni@oss.qualcomm.com>
3. **[02-10 19:03]** Re: [PATCH v2 00/35] KVM: arm64: Add support for protected guest
 memory with pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-12 10:37]** Re: [PATCH v2 14/35] KVM: arm64: Handle aborts from protected VMs
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[02-12 17:18]** Re: [PATCH v2 24/35] KVM: arm64: Introduce hypercall to force
 reclaim of a protected page
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[02-12 17:22]** Re: [PATCH v2 25/35] KVM: arm64: Reclaim faulting page from pKVM in
 spurious fault handler
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 9: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 6 Feb 2026 14:59:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM 架构的 KVM 添加 `kvm-psci-version` 虚拟 CPU 属性的补丁（PATCH v4 2/2）。该补丁旨在处理控制寄存器的相关问题，Sebastian Ott 在早期讨论中表示该补丁总体合理，并提到了一些与迁移失败相关的讨论。

在历史讨论中，Sebastian 提出了补丁的初步看法，并链接了与其他迁移失败处理的相关讨论。Peter Maydell 对此表示感谢，并表示已对之前的评论进行了处理，随后发布了补丁的 V5 版本。

在本周的新讨论中，Sebastian 和 Peter 继续探讨补丁的细节。Sebastian 提出了一种可能的情况，即如果迁移到一个不支持新 PSCI 版本的 QEMU，可能会出现问题。Peter 进一步澄清了补丁中的一个错误，指出在通过设置函数设置 QOM 属性后，读取其值时应返回刚刚写入的值。最后，Peter 提出了一个修正建议，展示了如何正确获取 PSCI 版本的代码实现。

总体来看，本周的讨论集中在补丁的细节修正和潜在问题的澄清上，推动了补丁的完善。

#### 📝 邮件列表

1. **[02-06 14:59]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
2. **[02-11 16:37]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[02-11 15:43]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
4. **[02-11 17:04]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 10: [PATCH] KVM: arm64: Allow module-owned pages in host stage-2 range adjustment

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 9 Feb 2026 11:24:13 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在允许模块拥有的页面在主机的第二阶段地址范围调整中被接受。补丁的主要内容是修改 `host_stage2_adjust_range()` 函数，以避免在处理模块拥有的页面时触发不必要的警告。

在历史讨论中，参与者没有提供具体的背景信息，但补丁的目的明确，即扩展对标记为 `PKVM_MODULE_OWNED_PAGE` 的页面的检查，以防止在正常的模块内存访问模式下出现虚假警告。

本周的新讨论中，Kyle Liao 提出了补丁，并指出当 `load_unaligned_zeropad()` 函数访问跨越页面边界的内存时，可能会遇到同时标记为 `PKVM_NOPAGE` 和 `PKVM_MODULE_OWNED_PAGE` 的页面。Marc Zyngier 回复表示该补丁在上游代码中并不存在。同时，内核测试机器人报告了构建错误，指出在补丁中使用的 `PKVM_MODULE_OWNED_PAGE` 标识符未被声明，导致编译失败。这提示补丁需要进一步修正以解决这些错误。

#### 📝 邮件列表

1. **[02-09 11:24]** [PATCH] KVM: arm64: Allow module-owned pages in host stage-2 range adjustment
   - 发件人: kyle-jk.liao <kyle-jk.liao@mediatek.com>
2. **[02-09 09:22]** Re: [PATCH] KVM: arm64: Allow module-owned pages in host stage-2 range adjustment
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-10 01:35]** Re: [PATCH] KVM: arm64: Allow module-owned pages in host stage-2
 range adjustment
   - 发件人: kernel test robot <lkp@intel.com>
4. **[02-10 06:44]** Re: [PATCH] KVM: arm64: Allow module-owned pages in host stage-2
 range adjustment
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 11: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 9 Feb 2026 13:14:07 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于优化 ARM64 架构下 KVM 的 TLB 刷新功能，具体是通过在 `kvm_tlb_flush_vmid_range` 函数中减少对 `kvm_call_hyp` 的调用次数来提高性能。

**原始 patch/问题内容**：
该 patch 提出了在进行大范围 TLB 刷新时，直接调用 `__kvm_tlb_flush_vmid`，以避免在地址范围超过 `MAX_TLBI_RANGE_PAGES` 时频繁进入 `kvm_call_hyp`，从而减少在实时迁移过程中性能损耗。

**之前讨论要点**：
在历史讨论中，未提供具体的讨论内容，但可以推测该 patch 的提出是基于对现有实现性能瓶颈的识别，尤其是在实时迁移场景下。

**本周的新讨论与进展**：
本周的讨论中，参与者 Marc Zyngier 对 patch 提出了几点质疑，包括缺乏合并所需的 SoB 标签、没有提供足够的数据来证明改动的有效性，以及缺乏测试描述。随后，yezhenyu 提供了性能数据，显示在应用该 patch 后，实时迁移带宽显著提升，从不足 10 GBps 增加到 50 GBps，表明该 patch 在优化迁移性能方面具有积极效果。yezhenyu 表示如果没有其他问题，将会在补充 SoB 标签后重新提交该 patch。

#### 📝 邮件列表

1. **[02-09 13:14]** [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range
   - 发件人: yezhenyu (A) <yezhenyu2@huawei.com>
2. **[02-09 14:35]** Re: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during kvm_tlb_flush_vmid_range
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-12 20:02]** Re: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range
   - 发件人: yezhenyu (A) <yezhenyu2@huawei.com>

---

### Thread 12: [PATCH v5 0/2] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 11 Feb 2026 16:30:30 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM 架构的 KVM 中添加 `kvm-psci-version` 虚拟 CPU 属性的补丁。这一补丁的目的是允许用户指定 KVM 使用的 PSCI（电源状态协调接口）版本，以支持在不同默认 PSCI 版本的主机内核之间进行虚拟机迁移。

在历史讨论中，补丁的初步版本经历了多次修改，主要集中在变量命名、代码修复和反馈整合上。参与者们对补丁的功能和实现进行了审查和测试，确保其能够兼容不同的 PSCI 版本。

本周的新讨论中，开发者 Sebastian Ott 提交了补丁的最新版本（v5），并详细说明了补丁的内容和变更。补丁中添加了对 PSCI 版本 1.2 和 1.3 的常量支持，并提供了一个新的虚拟 CPU 属性 `kvm-psci-version`，允许用户设置 PSCI 版本。当前支持的版本包括 0.1、0.2、1.0、1.1、1.2 和 1.3。开发者还指出，为了支持 PSCI v0.1，需要在某些情况下放弃对 KVM_CAP_ARM_PSCI_0_2 的初始化。

总体来看，本周的讨论主要集中在补丁的最终确认和功能实现上，开发者们对补丁的有效性和兼容性表示认可，并进行了必要的测试。

#### 📝 邮件列表

1. **[02-11 16:30]** [PATCH v5 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-11 16:30]** [PATCH v5 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[02-11 16:30]** [PATCH v5 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 13: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 5 Feb 2026 10:58:11 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于对 kvmtool 的一个补丁系列，主要目的是支持基于 GICv5 的 arm64 客户机。该补丁系列共有 17 个补丁，最初由 Sascha Bischoff 提出，并在 2026 年 2 月 5 日的邮件中进行了介绍。

在历史讨论中，Fuad Tabba 表达了对该补丁系列的审查和测试兴趣，并询问了补丁的可用性。Sascha 随后提供了补丁的链接，并提到了一些更新，包括帮助信息中新增了对 gicv5 的提及。

在本周的新讨论中，Fuad 确认了补丁的构建成功，并表示在 gicv5.yaml 文件中做了一些必要的更改，确保系统能够正常启动。Fuad 对 Sascha 的工作表示感谢，并确认了补丁的有效性。

总体来看，本周的讨论显示出补丁的顺利进展，参与者对补丁的认可和支持，为后续的测试和应用奠定了基础。

#### 📝 邮件列表

1. **[02-05 10:58]** Re: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[02-05 18:23]** Re: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[02-09 07:54]** Re: [PATCH kvmtool v2 00/17] arm64: Support GICv5-based guests
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 14: [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Feb 2026 14:30:23 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为处理 gic_kvm_info 分配类型中的 const 限定符。

1. **原始 patch/问题的内容**：Kees Cook 提出的补丁旨在确保 kmalloc 分配器返回的类型与被赋值变量的类型匹配。之前，分配器总是返回 "void *"，需要通过使用解引用指针来确保返回类型与 "struct gic_kvm_info" 完全一致，以解决 const 限定符的问题。

2. **之前讨论要点**：在历史讨论中，Kees Cook 详细阐述了补丁的必要性，强调了类型匹配的重要性，以便为即将进行的类型感知分配器做准备。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Marc Zyngier 确认了补丁的应用，并表示已将其合并到修复分支中，感谢 Kees Cook 的贡献。这表明该补丁已成功通过审核并进入代码库。

总的来说，此次讨论集中在确保内存分配类型的准确性上，补丁已获得批准并实施。

#### 📝 邮件列表

1. **[02-06 14:30]** [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type
   - 发件人: Kees Cook <kees@kernel.org>
2. **[02-13 15:03]** Re: [PATCH v2] KVM: arm64: vgic: Handle const qualifier from gic_kvm_info allocation type
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 13 Feb 2026 14:16:19 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构中强制使用 CNTVCT_EL0 进行延迟函数 `__delay()` 的修复补丁。

**原始 patch/问题的内容**：
Marc Zyngier 提出的补丁旨在解决在 KVM 虚拟化环境下，使用 WFxT 进行延迟时出现的问题。当 vcpu 被加载且 KVM 不处于 VHE 模式时，CNTVOFF_EL2 被设置为非零值，导致 `__delay()` 函数使用的物理计数器与虚拟计数器之间存在显著差异。

**之前讨论要点**：
在历史讨论中，补丁的背景是由于 CNTVOFF_EL2 的偏移量未重置为零，造成了计数器读取不一致的问题。补丁的提出是为了确保在不同的 KVM 模式下，`__delay()` 函数能够一致地使用 CNTVCT_EL0，避免因使用不同计数器而引发的错误。

**本周的新讨论、进展或结论**：
本周的讨论中，Marc Zyngier 详细说明了补丁的实现细节，强调了强制使用 CNTVCT_EL0 的必要性，以确保在 KVM 主机运行时的延迟函数表现一致。补丁已被审核并准备提交，预计将解决当前存在的计数器不一致问题。

#### 📝 邮件列表

1. **[02-13 14:16]** [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 12 Feb 2026 10:48:47 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 中支持 Arm CCA 的补丁（PATCH v12 00/46）。本周的讨论主要集中在补丁的编译问题和在 FVP 模拟器上运行的测试结果。

在本周的讨论中，参与者 Mathieu Poirier 提到，之前的分支 cca/v10 存在编译问题，因为函数 realm_configure_parameters() 没有被调用。通过将该函数标记为 [[maybe_unused]]，他解决了编译问题。此外，他在 FVP 模拟器上测试了包含 EDK2 的 Realm 启动堆栈，结果成功启动。然而，当直接从 lkvm 启动内核且不包含 EDK2 时，挂载 initrd 失败。经过进一步调查，发现从 Realm 内核的角度来看，initrd 的内容要么被加密，要么被覆盖。

Mathieu 表示愿意提供更多细节，以便深入探讨这个问题。总体来看，本周的讨论主要关注补丁的编译修复和在模拟器上的运行情况，显示出对补丁的进一步测试和问题解决的努力。

#### 📝 邮件列表

1. **[02-12 10:48]** Re: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Mathieu Poirier <mathieu.poirier@linaro.org>

---

### Thread 17: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 12 Feb 2026 11:54:08 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 arm64 架构的补丁（patch），该补丁旨在优化 KVM 的 TLB 刷新操作，特别是在 `kvm_tlb_flush_vmid_range` 函数中调用 `kvm_call_hyp` 的频率。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是为了提升 KVM 在虚拟机迁移过程中的性能，尤其是减少 TLB 刷新的开销。

本周的新讨论中，参与者 Marc Zyngier 提供了补丁应用前后的性能对比数据。通过性能分析图（flame graph），他指出在进行实时迁移时，`ram_find_and_save_block()` 函数的执行时间显著降低，应用补丁后，该函数的执行时间从 84.01% 降至 53.84%。同时，`memory_region_clear_dirty_bitmap()` 和 `kvm_clear_dirty_log_protect()` 的执行时间也大幅减少，表明补丁有效地优化了迁移带宽。在没有补丁的情况下，迁移带宽低于 10 GBps，而应用补丁后，迁移带宽提升至 50 GBps。

Marc 表示，如果没有其他问题，他将带上签名重新提交该补丁。这表明补丁的效果得到了积极的验证，并有望在未来的版本中得到应用。

#### 📝 邮件列表

1. **[02-12 11:54]** Re: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range
   - 发件人: yezhenyu (A) <yezhenyu2@huawei.com>

---

### Thread 18: [PATCH v9 10/30] KVM: arm64: Document the KVM ABI for SME

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 9 Feb 2026 15:18:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 SME（Scalable Matrix Extension）相关的 ABI（Application Binary Interface）文档。原始的 patch 提出对 KVM 的 SME ABI 进行文档化，以便更好地支持该架构的虚拟化功能。

在之前的讨论中，虽然没有具体的历史邮件记录，但可以推测该 patch 的目的是为了提供清晰的文档，帮助开发者理解和实现 SME 的相关功能。

在本周的新讨论中，参与者 Peter Maydell 对 patch 的封面信和文档内容之间的矛盾提出了疑问。他指出封面信中提到的内容与文档 patch 本身的表述不一致，询问作者 Mark Brown 哪一部分才是其真实意图。这表明在文档的准确性和一致性方面仍需进一步澄清和确认。

#### 📝 邮件列表

1. **[02-09 15:18]** Re: [PATCH v9 10/30] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Peter Maydell <peter.maydell@linaro.org>

---

### Thread 19: [PATCH kvmtool v5 0/7] arm64: Nested virtualization support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 9 Feb 2026 11:21:19 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于对 KVM 工具的补丁，旨在为 arm64 架构提供嵌套虚拟化支持。该补丁系列包含七个部分，具体内容在邮件中未详细列出。

在之前的讨论中，参与者们可能探讨了补丁的设计思路、实现细节及其对现有虚拟化功能的影响。然而，由于本周没有提供历史讨论的具体内容，无法详细总结之前的讨论要点。

本周的新讨论中，Itaru Kitayama 向 Andre Przywara 提出了一个问题，询问他是否在最新的 QEMU 版本中测试过该补丁系列，特别是 QEMU 的 FEAT_NV2 支持。他提到在尝试使用 lkvm 创建嵌套虚拟机时遇到了卡住的问题。这表明在实际应用中可能存在问题，提示需要进一步的测试和调试。

总的来说，本周的讨论集中在对补丁的测试效果及其与 QEMU 兼容性的问题上，反映出对嵌套虚拟化功能的关注和对补丁稳定性的期望。

#### 📝 邮件列表

1. **[02-09 11:21]** Re: [PATCH kvmtool v5 0/7] arm64: Nested virtualization support
   - 发件人: Itaru Kitayama <itaru.kitayama@fujitsu.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 updates for 7.0

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Feb 2026 15:33:45 +0000

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 7.0 版本的更新内容。历史讨论中，Marc Zyngier 提出了一个补丁集，主要包括两个方面的更新：首先是针对 pKVM 的一系列修复，确保不向来宾或主机暴露的功能确实无法访问；其次是对寄存器清理基础设施的大规模重构，包括对新寄存器的清理工作。此外，还有一些随机的低优先级更改，具体细节在邮件中有所提及。

在本周的新讨论中，Paolo Bonzini 对 Marc 的补丁集表示已完成处理，并表示感谢。这表明补丁集得到了认可，并可能会在后续版本中应用。

总体来看，本周的讨论主要是对历史补丁的确认和感谢，未涉及新的技术问题或深入讨论。

#### 📝 邮件列表

1. **[02-06 15:33]** [GIT PULL] KVM/arm64 updates for 7.0
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-09 18:19]** Re: [GIT PULL] KVM/arm64 updates for 7.0
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 2 个 thread

---

### Thread 1: [kvmtool PATCH v5 00/15] arm64: Handle PSCI calls in userspace

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon,  9 Feb 2026 16:25:56 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在用户空间处理 PSCI 调用的补丁（patch），具体为 kvmtool 的第 5 版补丁集（v5 00/15）。补丁的主要内容是允许在虚拟机（VM）中通过 vcpu 线程进行暂停操作。

在之前的讨论中，虽然没有详细的历史记录，但可以推测该补丁是为了增强 kvmtool 在 ARM64 架构下的功能，特别是与电源管理相关的 PSCI 调用的处理能力。

在本周的新讨论中，参与者 Will Deacon 确认已将补丁中的第一部分应用到 kvmtool 的主分支中，并感谢补丁的贡献。具体的补丁链接为 [01/15]，其功能是允许通过 vcpu 线程暂停虚拟机。这表明该补丁的开发进展顺利，并且已经开始被实际应用。

#### 📝 邮件列表

1. **[02-09 16:25]** Re: [kvmtool PATCH v5 00/15] arm64: Handle PSCI calls in userspace
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 2: [kvmtool PATCH v5 02/15] update_headers: arm64: Track psci.h for
 PSCI definitions

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 9 Feb 2026 15:51:37 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于更新 KVM 工具中 arm64 架构的 PSCI 定义头文件的补丁。原始补丁的目的是追踪 psci.h 文件，以便更好地支持 PSCI 定义。

在历史讨论中，参与者 Suzuki K Poulose 提出了对补丁内容的疑问，认为目前并不存在 arm64 的 uapi/asm/psci.h 文件，并且不清楚补丁中提到的更改如何与即将引入的 linux/psci.h 文件相结合。他建议先应用第一个补丁，然后自行使用当前脚本将头文件更新到版本 6.19，因为其他人也需要进行更新。

在本周的新讨论中，Will Deacon 对 Suzuki 的观点表示认同，并决定先应用补丁，再手动更新头文件。这表明参与者们在补丁的有效性和必要性上存在分歧，但最终达成了一致的行动计划，以确保头文件的更新能够满足需求。

#### 📝 邮件列表

1. **[02-09 15:51]** Re: [kvmtool PATCH v5 02/15] update_headers: arm64: Track psci.h for
 PSCI definitions
   - 发件人: Will Deacon <will@kernel.org>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: Broken udelay() on KVM host with a vcpu loaded

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 10 Feb 2026 12:27:48 +0000

#### 🤖 AI 总结

本邮件线程讨论了在 KVM 主机上运行 vCPU 时，`udelay()` 函数出现的问题。该问题源于使用 WFxT 的 `__delay()` 函数在 vCPU 加载时不一致地读取计时器值，导致延迟计算错误。Quentin Perret 首先提出了该问题，并建议两种解决方案：一是提前切换 KVM 上下文以确保正确的计时器使用，二是修改 `udelay()` 实现以直接读取 CNTVCT_EL0。

Marc Zyngier 随后提出了一个补丁，强制 `__delay()` 使用 CNTVCT_EL0，从而确保在不同上下文中计时器的一致性。他认为第一种方案复杂且可能影响性能，而第二种方案更为可行。Will Deacon 也参与了讨论，提出了避免在 vCPU 加载时使用 WFxT 的想法，并讨论了用户空间对计时器偏移的控制问题。

本周的讨论中，参与者们一致认为 vCPU 互斥锁可以防止在运行 vCPU 时出现问题，并确认了补丁的有效性。最终，Quentin 对补丁进行了审核，并建议在补丁中添加注释以澄清锁定机制。该补丁有望解决 `udelay()` 在 KVM 主机上的不一致性问题。

#### 📝 邮件列表

1. **[02-10 12:27]** Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Quentin Perret <qperret@google.com>
2. **[02-10 12:52]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-10 15:34]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Will Deacon <will@kernel.org>
4. **[02-10 15:58]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Quentin Perret <qperret@google.com>
5. **[02-10 19:46]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-10 19:54]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-13 11:50]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Will Deacon <will@kernel.org>
8. **[02-13 13:52]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-13 14:05]** Re: Broken udelay() on KVM host with a vcpu loaded
   - 发件人: Quentin Perret <qperret@google.com>

---

